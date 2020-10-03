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