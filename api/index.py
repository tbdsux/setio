from sanic import Sanic
from sanic.response import json

# utils
import requests
import os
from dotenv import load_dotenv
load_dotenv()

base_url = "http://api.openweathermap.org/data/2.5/weather?q="

class Weather:
    @staticmethod
    def Get(city_id):
        resp = requests.get(base_url + city_id + "&appid=" + os.getenv("OPENWEATHER")).json()

        return [resp['name'], resp['sys']['country'], resp['weather'][0]['main'], resp['weather'][0]['description'], Weather.convert_temp(resp['main']['temp']), Weather.convert_temp(resp['main']['feels_like']), Weather.convert_temp(resp['main']['temp_min']), Weather.convert_temp(resp['main']['temp_max'])]

    # conver the temperature from kelvin to celcius
    @staticmethod
    def convert_temp(kelvin_temp):
        return round(kelvin_temp - 273.15)

app = Sanic(name="setio")

@app.route("/")
@app.route("/<path:string>")
async def index(request, path=""):
    return json({"hello": path})

@app.route("/weather/<city_id:string>")
async def weather(request, city_id=""):
    weather = Weather.Get(city_id)
    __message = {
        "messages": [
            {"text": f"Weather for *{weather[0]}, {weather[1]}*"},
            {"text": f"It feels like *{weather[5]}C* _({weather[4]}C)_."},
            {"text": f"The weather is *{weather[2]}* ({weather[3]}) with a maximum temperature of *{weather[7]}C* and a minimum temperature of *{weather[6]}C*."}
        ]
    }

    return json(__message)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000)