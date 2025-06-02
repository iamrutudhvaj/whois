from fastapi import APIRouter

from app.services.whois_service import (
    fetch_whois_data,
    process_contact_data,
    process_domain_data,
)

router = APIRouter()


@router.post("/whois")
async def create_whois_record(request_data: dict):
    # Get the domain name from the request data or use a default
    domain_name = request_data.get("domain_name", "amazon.com")
    data_type = request_data.get("data_type", "domain")

    # Fetch WHOIS data
    data = await fetch_whois_data(domain_name)
    whois_record = data.get("WhoisRecord", {})

    # Process data based on data_type
    if data_type == "domain":
        return process_domain_data(whois_record, domain_name)
    elif data_type == "contact":
        return process_contact_data(whois_record, domain_name)
    else:
        # Return the full data if data_type is not recognized
        return data
