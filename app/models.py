import requests
import os

api_key = os.environ.get("OWM_API_KEY")
lat = "51.924419"
lon = "4.477733"

class Weathermodel():
    @staticmethod
    def get_weather_data():
        url=f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the JSON response
            weather_data = response.json()

    # Extract the relevant information for the next few timestamps
            forecasts = weather_data.get('list', [])
            return forecasts


        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
