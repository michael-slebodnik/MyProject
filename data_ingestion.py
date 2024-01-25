# data_ingestion.py
import requests
import time

while True:
    api_key = "5835a1191aaab7189120d5f9747d5a53"
    lat = "40.7128"
    lon = "-74.0060"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    # Process and store data in MongoDB

    time.sleep(60*60)  # Fetch data every hour

