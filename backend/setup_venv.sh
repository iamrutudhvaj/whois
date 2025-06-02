#!/bin/zsh

# Install uv if not already installed
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

# Create virtual environment using uv
echo "Creating virtual environment with uv..."
uv venv .venv

# Activate the virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Install dependencies using uv
echo "Installing dependencies from requirements.txt..."
uv pip install -r requirements.txt

# Check if installation was successful
if [ $? -eq 0 ]; then
    echo "Virtual environment setup complete!"
    echo "To activate the virtual environment, run: source .venv/bin/activate"
else
    echo "Error installing dependencies"
    exit 1
fi
