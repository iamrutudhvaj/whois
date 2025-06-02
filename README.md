# WHOIS Domain Lookup

A full-stack web application for looking up WHOIS information for domains. The application consists of a FastAPI backend that fetches WHOIS data from external APIs and a React frontend that provides a user-friendly interface for domain lookups.

## Project Overview

This project provides a simple and efficient way to look up domain registration information. Users can search for domain details or contact information associated with a domain.

### Features

- Domain information lookup (registrar, registration date, expiration date, etc.)
- Contact information lookup (registrant, technical contact, administrative contact)
- Responsive UI built with React and Tailwind CSS
- RESTful API built with FastAPI

## Using the Makefile

This project includes a Makefile that simplifies common development tasks. You can use the following commands:

```bash
# Set up both backend and frontend environments
make setup

# Start both backend and frontend services with a single command
make start

# Start only the backend service
make backend

# Start only the frontend service
make frontend

# Stop all running services
make stop

# Clean up generated files and directories
make clean

# Run tests for both backend and frontend
make test

# Display all available commands
make help
```

Using the Makefile is the recommended way to run the application as it handles both backend and frontend services with a single command.

## Project Structure

```
whois/
├── backend/                 # FastAPI Backend
│   ├── app/                 # Application package
│   │   ├── api/             # API endpoints
│   │   ├── services/        # Business logic
│   │   └── utils/           # Utility functions
│   ├── main.py              # Application entry point
│   ├── requirements.txt     # Python dependencies
│   ├── run.sh               # Script to run the application
│   └── setup_venv.sh        # Script to set up virtual environment
│
└── frontend/                # React Frontend
    ├── public/              # Static files
    ├── src/                 # Source code
    │   ├── components/      # React components
    │   ├── App.js           # Main application component
    │   └── index.js         # Entry point
    ├── package.json         # JavaScript dependencies
    └── tailwind.config.js   # Tailwind CSS configuration
```

## Prerequisites

- Python 3.8 or higher
- Node.js 14.0 or higher
- npm 6.0 or higher
- Git

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Clone the Repository

```bash
git clone https://github.com/iamrutudhvaj/whois.git
cd whois
```

### Backend Setup

1. Navigate to the backend directory:

```bash
cd backend
```

2. Set up a Python virtual environment:

```bash
chmod +x setup_venv.sh
./setup_venv.sh
```

3. Activate the virtual environment:

```bash
source .venv/bin/activate
```

4. Create a `.env` file in the backend directory:

```bash
echo "WHOIS_API_KEY=your_api_key_here" > .env
```

Replace `your_api_key_here` with your actual WHOIS XML API key. See the `API_KEY_GUIDE.md` file for instructions on obtaining an API key.

5. Start the backend server:

```bash
chmod +x run.sh
./run.sh
```

The backend server will run on http://localhost:8000.

6. (Optional) Test the API:

```bash
python test_api.py
```

This will send a test request to the backend API and display the response.

### Frontend Setup

1. Navigate to the frontend directory:

```bash
cd ../frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the development server:

```bash
npm start
```

The frontend application will run on http://localhost:5000.

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

## Development

### Backend Development

- The backend is built with FastAPI
- Environment variables are loaded from a `.env` file
- CORS is enabled for frontend development

### Frontend Development

- The frontend is built with React
- Styling is done with Tailwind CSS
- API calls are made using Axios

## Environment Variables

### Backend

- `WHOIS_API_KEY`: Your WHOIS XML API key (required for production)

## Troubleshooting

- If you encounter CORS issues, ensure the backend CORS middleware is properly configured
- If the API returns errors, check your WHOIS_API_KEY in the .env file
- For frontend issues, check the browser console for error messages

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [React](https://reactjs.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [WHOIS XML API](https://www.whoisxmlapi.com/)
