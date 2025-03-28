import requests
import json

def fetch_today_earthquakes():
    # USGS API endpoint for earthquakes in the last 24 hours
    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["features"]  # Extract list of earthquakes
    else:
        print(f"Error: {response.status_code}")
        return None

# Fetch earthquake data for today
earthquakes = fetch_today_earthquakes()

# Print formatted results
if earthquakes:
    print(f"Total earthquakes today: {len(earthquakes)}")
    for quake in earthquakes:
        props = quake["properties"]
        print(f"Location: {props['place']}, Magnitude: {props['mag']}, Time: {props['time']}")
else:
    print("No earthquake data available for today.")
