import requests
import json
import ast 
from geopy.geocoders import Nominatim
countries = [
    "Malaysia", "Singapore", "Vietnam", "Laos", "Cambodia",
    "Myanmar", "Indonesia", "India", "Bangladesh", "China"
]
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
        #print(f"Location: {props['place']}, Magnitude: {props['mag']}, Time: {props['time']}")
        mapdat = props['place'].split("of")
        try:  
            print("Country data: ",mapdat[1].split(","),props['place'])
            print("Processing country extract: ",mapdat[1].split(",")[1].split(" ")[1])
            city_name = mapdat[1].split(",")[1].split(" ")[1]
            print("City name: ",city_name)
            print("Payload data: ",props)
            '''
            #geolocator = Nominatim(user_agent="kornbot380@hotmail.com") #Get the locator 
            location = geolocator.geocode(city_name) 
            if location:
                 print(f"City: {city_name}")
                 print(f"Full Address: {location.address}")
                 print(f"Latitude: {location.latitude}")
                 print(f"Longitude: {location.longitude}")
                 # Access detailed info (address dictionary)
                 location_detail = geolocator.reverse((location.latitude, location.longitude), language='en')
                 country = location_detail.raw['address'].get('country')
                 print(f"Country: {country}")

            else:
                print("City not found.")
            '''
        except:
            print("Country data: ",mapdat,props['place'][0])
else:
    print("No earthquake data available for today.")
