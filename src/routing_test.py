import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTE_API_KEY")

start = [4.4012, 51.21911]
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

route = data["routes"][0]

duration_seconds = route["summary"]["duration"]
distance_meters = route["summary"]["distance"]



match duration_seconds:
    case d if d >= 86400:
        print(f"Duration: {int(duration_seconds/86400)} d {round((duration_seconds/86400-int(duration_seconds/86400))*24)} h")
    case d if 3600 <= d < 86400:
        print(f"Duration: {int(duration_seconds/3600)} h {round((duration_seconds/3600-int(duration_seconds/3600))*60)} min")
    case d if d < 3600:
        print(f"Duration: {round(duration_seconds / 60)} min")

match distance_meters:
    case d if d >= 10000:
        print(f"Distance: {round(distance_meters / 1000)} km")
    case d if 1000 <= d < 10000:
        print(f"Distance: {round(distance_meters / 1000, 1)} km")
    case d if d < 1000:
        print(f"Distance: {round(int(distance_meters/10)*10)} m")