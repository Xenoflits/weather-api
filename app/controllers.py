from app.models import Weathermodel

class Weathercontroller:
    @staticmethod
    def fetch_weather():
        return Weathermodel.get_weather_data()