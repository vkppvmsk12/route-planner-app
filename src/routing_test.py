import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTE_API_KEY")

start = [4.4212, 51.21711]
end = [4.401597, 51.219047]

url = "https://api.openrouteservice.org/v2/directions/foot-walking"

headers = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}

body = {
    "coordinates": [start, end]
}

response = requests.post(url, json=body, headers=headers)

data = response.json()
print(type(response))