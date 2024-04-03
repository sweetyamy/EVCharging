import requests
import os

api_key = OS.getenv("NREL_API_KEY")

# Perfom GET request using Requests
req_url = "https://developer.nrel.gov/api/alt-fuel-stations/v1.json?{}".format(api_key)

response = requests.get(req_url)

print(response)
print("=" * 50)
print(response.content)