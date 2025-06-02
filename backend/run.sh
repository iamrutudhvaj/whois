#!/bin/zsh

# Activate the virtual environment
source .venv/bin/activate

# Run the FastAPI application using uvicorn
echo "Starting FastAPI server..."
uvicorn main:app --reload --host 0.0.0.0 --port 8000
