import os

import httpx
from fastapi import HTTPException, status

from app.utils.domain_utils import calculate_domain_age, format_hostnames


async def fetch_whois_data(domain_name):
    """Fetches WHOIS data from external API"""
    third_party_url = "https://www.whoisxmlapi.com/whoisserver/WhoisService"

    # Use environment variable for API key
    api_key = os.environ.get("WHOIS_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="WHOIS_API_KEY environment variable is not set",
        )

    try:
        # Async call to third-party API
        async with httpx.AsyncClient() as client:
            response = await client.get(
                third_party_url,
                params={
                    "outputFormat": "JSON",
                    "domainName": domain_name,
                    "apiKey": api_key,
                },
            )

        # Check for HTTP errors
        response.raise_for_status()

        # Check response content before parsing JSON
        if not response.content:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail="Empty response from WHOIS API",
            )

        try:
            # Access data (assuming JSON response)
            data = response.json()

            # Check if there's an error message in the response
            if "ErrorMessage" in data:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"WHOIS API error: {data['ErrorMessage']}",
                )

            # Check for non-existent domain (based on the provided response format)
            whois_record = data.get("WhoisRecord", {})
            if (
                "dataError" in whois_record
                and whois_record.get("dataError") == "MISSING_WHOIS_DATA"
            ):
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Domain not found: {domain_name} does not exist or is not registered",
                )

            return data

        except ValueError as json_error:
            # Handle JSON decode errors
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail=f"Invalid JSON response from WHOIS API: {str(json_error)}",
            )

    except httpx.HTTPStatusError as e:
        # Handle HTTP status errors from the API
        status_code = e.response.status_code
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"WHOIS API returned error status {status_code}: {e.response.text}",
        )
    except httpx.RequestError as e:
        # Handle connection errors, timeouts, etc.
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Error connecting to WHOIS API: {str(e)}",
        )
    except Exception as e:
        # Catch-all for any other errors
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error processing WHOIS data: {str(e)}",
        )


def process_domain_data(whois_record, domain_name):
    """Process WHOIS data for domain information"""
    if not whois_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No WHOIS record found for domain: {domain_name}",
        )

    domain_info = {
        "Domain Name": whois_record.get("domainName", "N/A"),
        "Registrar": whois_record.get("registrarName", "N/A"),
        "Registration Date": whois_record.get("createdDate", "N/A"),
        "Expiration Date": whois_record.get("expiresDate", "N/A"),
        "Estimated Domain Age": calculate_domain_age(
            whois_record.get("createdDate", "")
        ),
        "Hostnames": format_hostnames(
            whois_record.get("nameServers", {}).get("hostNames", [])
        ),
    }
    return domain_info


def process_contact_data(whois_record, domain_name):
    """Process WHOIS data for contact information"""
    if not whois_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No WHOIS record found for domain: {domain_name}",
        )

    registrant = whois_record.get("registrant", {})
    admin_contact = whois_record.get("administrativeContact", {})
    tech_contact = whois_record.get("technicalContact", {})

    contact_info = {
        "Registrant Name": registrant.get("name", "N/A"),
        "Technical Contact Name": tech_contact.get("name", "N/A"),
        "Administrative Contact Name": admin_contact.get("name", "N/A"),
        "Contact Email": registrant.get("email", "N/A"),
    }
    return contact_info
