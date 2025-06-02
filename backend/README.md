# WHOIS API Service

A FastAPI-based service that provides domain WHOIS information through a clean RESTful API.

## Project Structure

The project has been organized into a modular structure:

```
backend/
├── app/                    # Application package
│   ├── api/                # API endpoints
│   │   └── whois.py        # WHOIS API endpoint
│   ├── services/           # Business logic
│   │   └── whois_service.py # WHOIS data fetching and processing
│   └── utils/              # Utility functions
│       └── domain_utils.py  # Domain-related utilities
├── main.py                 # Application entry point
├── requirements.txt        # Project dependencies
├── run.sh                  # Script to run the application
└── setup_venv.sh           # Script to set up virtual environment
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository
2. Set up a virtual environment:

```bash
./setup_venv.sh
```

3. Activate the virtual environment:

```bash
source .venv/bin/activate
```

### Running the Application

Start the application using the provided script:

```bash
./run.sh
```

Or manually:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## API Usage

### WHOIS Information Endpoint

```
POST /api/whois
```

Request Body:

```json
{
  "domain_name": "example.com",
  "data_type": "domain"  // Options: "domain", "contact"
}
```

Example Response (domain data):

```json
{
  "Domain Name": "example.com",
  "Registrar": "Example Registrar, LLC",
  "Registration Date": "1995-08-14T04:00:00Z",
  "Expiration Date": "2023-08-13T04:00:00Z",
  "Estimated Domain Age": "28 years",
  "Hostnames": "a.iana-servers.net, b.ia..."
}
```

## Environment Variables

For production use, set the following environment variables:

- `WHOIS_API_KEY`: Your WHOIS XML API key

### Using .env file

The application uses python-dotenv to load environment variables from a .env file in the project root. Create a .env file with the following format:

```
WHOIS_API_KEY=your_api_key_here
```

This method is suitable for development. For production, use proper environment variable management appropriate for your deployment platform.

## License

This project is licensed under the MIT License.
