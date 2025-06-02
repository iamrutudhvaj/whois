from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.whois import router as whois_router

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for simplicity; adjust as needed
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Include routers
app.include_router(whois_router, prefix="/api", tags=["whois"])


# For development purposes, you can add a root endpoint
@app.get("/")
async def root():
    return {"message": "WHOIS API Service is running"}
