import requests
import os
from dotenv import load_dotenv
load_dotenv()

base_url = "http://api.openweathermap.org/data/2.5/weather?q="

class Weather:
    @staticmethod
    def Get(city_id):
        resp = requests.get(base_url + city_id + "&appid=" + os.getenv("OPENWEATHER")).json()

        if resp["cod"] == "404":
            return [resp["cod"]]

        return [resp['name'], resp['sys']['country'], resp['weather'][0]['main'], resp['weather'][0]['description'], Weather.convert_temp(resp['main']['temp']), Weather.convert_temp(resp['main']['feels_like']), Weather.convert_temp(resp['main']['temp_min']), Weather.convert_temp(resp['main']['temp_max'])]

    # conver the temperature from kelvin to celcius
    @staticmethod
    def convert_temp(kelvin_temp):
        return round(kelvin_temp - 273.15)