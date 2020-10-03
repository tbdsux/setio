from sanic import Sanic
from sanic.response import json

# utils
from .weather import Weather

app = Sanic(name="setio")

@app.route("/")
@app.route("/<path:string>")
async def index(request, path=""):
    return json({"hello": path})

@app.route("/weather/<city_id:string>")
async def weather(request, city_id=""):
    weather = Weather.Get(city_id)

    if weather[0] != "404":
        __message = {
            "messages": [
                {"text": f"Weather for *{weather[0]}, {weather[1]}* \n\nIt feels like *{weather[5]}°C* ({weather[4]}°C).\n\nThe weather is *{weather[2]}* ({weather[3]}) with a maximum temperature of *{weather[7]}°C* and a minimum temperature of *{weather[6]}°C*."}
            ]
        }
    else:
        __message = {
            "messages": [
                {"text": "Sorry but that city or municipality cannot be found."}
            ]
        }

    return json(__message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)