import re
from datetime import datetime


def calculate_domain_age(created_date):
    """Calculate the age of a domain from its creation date"""
    print(f"Calculating domain age for created date: {created_date}")
    if not created_date:
        return "N/A"

    try:
        # Handle various date formats that might come from WHOIS data
        # Remove any time zone indicators or extra parts
        created_date = re.sub(r"\s*\([^)]*\)", "", created_date)
        created_date = created_date.strip()

        # Try multiple date formats
        date_formats = [
            "%Y-%m-%dT%H:%M:%S%z",  # ISO format with timezone offset (like +0000)
            "%Y-%m-%dT%H:%M:%SZ",  # ISO format with Z
            "%Y-%m-%dT%H:%M:%S.%fZ",  # ISO format with milliseconds and Z
            "%Y-%m-%d %H:%M:%S",  # Standard datetime
            "%Y-%m-%d",  # Simple date
            "%d-%b-%Y",  # Format like 12-Jan-2000
            "%d.%m.%Y",  # European format
        ]

        created_datetime = None
        for fmt in date_formats:
            try:
                created_datetime = datetime.strptime(created_date, fmt)
                break
            except ValueError:
                continue

        if not created_datetime:
            return "N/A"

        # Calculate the age
        current_datetime = datetime.now()
        years_diff = current_datetime.year - created_datetime.year
        months_diff = current_datetime.month - created_datetime.month

        # Adjust if we haven't reached the month/day yet in the current year
        if months_diff < 0 or (
            months_diff == 0 and current_datetime.day < created_datetime.day
        ):
            years_diff -= 1
            months_diff = 12 + months_diff

        if years_diff > 0:
            return f"{years_diff} years"
        else:
            return "Less than a year"

    except Exception:
        return "N/A"


def format_hostnames(hostnames):
    """Format hostnames list, truncating if too long"""
    if not hostnames:
        return "N/A"

    # Join hostnames with commas
    formatted = ", ".join(hostnames)

    # Truncate if longer than 25 characters
    if len(formatted) > 25:
        return formatted[:22] + "..."

    return formatted