# merge JSON data from two different weather APIs
import requests
import json

url_1="https://api.open-meteo.com/v1/forecast?latitude=12.9719&longitude=77.5937&hourly=temperature_2m,weather_code"

url_2="https://api.open-meteo.com/v1/forecast?latitude=20.2724&longitude=85.8338&hourly=temperature_2m,weather_code"
try:
    response_1 = requests.get(url_1, timeout=5)
    response_1.raise_for_status()
    response_2 = requests.get(url_2, timeout=5)
    response_2.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    exit(1) 

data_1 = response_1.json()
data_2 = response_2.json()

merged = {
    "location_1": data_1,
    "location_2": data_2
}

with open('merged_weather.json', 'w') as f:
    json.dump(merged, f, indent=4)

