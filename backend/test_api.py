#!/usr/bin/env python3
import asyncio

import httpx


async def test_api():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:8000/api/whois", json={"domain_name": "google.com"}
            )

            print(f"Status Code: {response.status_code}")
            if response.status_code == 200:
                print("Response Data:")
                print(response.json())
            else:
                print("Error Response:")
                print(response.text)
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    asyncio.run(test_api())
