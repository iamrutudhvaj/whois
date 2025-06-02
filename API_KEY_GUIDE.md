# How to Get a WHOIS API Key

This guide will help you obtain a WHOIS API key to use with this application.

## Steps to Obtain a WHOIS API Key

1. **Visit WHOIS XML API Website**:
   - Go to https://www.whoisxmlapi.com/

2. **Create an Account**:
   - Click on "Sign Up" or "Create Account"
   - Fill in the required information to create your account
   - Verify your email address if required

3. **Choose a Plan**:
   - WHOIS XML API offers various plans, including a free tier with limited requests
   - Select the plan that meets your needs
   - For testing purposes, the free tier should be sufficient

4. **Access Your API Key**:
   - After signing up and selecting a plan, navigate to your account dashboard
   - Look for "API Keys" or "User Configuration" section
   - Copy your API key

## Setting Up Your API Key in the Application

1. **Create a .env File**:
   - Navigate to the backend directory of the project
   - Create a file named `.env` in this directory

2. **Add Your API Key**:
   - Open the `.env` file in a text editor
   - Add the following line, replacing `your_api_key_here` with your actual API key:
     ```
     WHOIS_API_KEY=your_api_key_here
     ```
   - Save the file

3. **Restart the Backend**:
   - If the backend server is already running, stop it and restart it
   - The application will now use your API key for WHOIS requests

## Troubleshooting

- If you receive errors about missing API keys, double-check that your `.env` file is in the correct location and contains the proper key-value pair
- Ensure the backend is restarted after adding or changing the API key
- Verify that your API key is active and has not exceeded its usage limits
- Check the console for specific error messages that might indicate issues with your API key
