# Importerar funtionen som använder Google Maps Geocoding API
from geocoding_api import get_coordinates
# Importerar funktionen som använder SMHI's API
from smhi_api import get_weather_forecast
# Importerar funktionen som använder Spotify's API
from spotify_api import get_spotify_info
# Importerar funktionen som hämtar vädersymbolerna från smhi
from weather import get_weather_picture
from flask import Flask, request, render_template
from flask import *

app = Flask(__name__)

@app.route('/')
def start():
    #visar startsidan där stad väljs, skickas vidare till route result
    return render_template("index.html")

@app.route('/result/', methods=['GET','POST'])
def find_city():
    # hämtar vilken stad som har angivits i formuläret
    city = request.form.get("city").title()
    # get_coordinates anropas med staden som argument för att ta fram koordinater
    # En lista innehållandes longitude och latitude returneras
    coordinates_list = get_coordinates(city)
    # get_weather_forecast anropas med koordinaterna som argument
    # En lista innehållandes temperatur och nuvarande vädersymbol returneras
    weather_forecast = get_weather_forecast(coordinates_list[0], coordinates_list[1])
    #tar ut endast vädersymbolen från weather_forecast.
    #SKa skickas till spotify och returneras i html result.
    weather_symbol = (weather_forecast['weather_symbol'])
    #tar ut endast temperaturen från weather_forecast
    #ska returneras till html result
    temp = (weather_forecast['temperature'])

    #hämtar ut bilden för vädersymbolen
    picture = get_weather_picture(weather_symbol)

    #get_spotify_info returnerar lista namnet på spellistan och länken till seplaren
    spotify_data = get_spotify_info(weather_symbol)
    name_of_playlist = spotify_data[0]
    link = spotify_data[1]

    return render_template("result.html", city=city, weather_symbol=weather_symbol, temp=temp, picture=picture, name_of_playlist=name_of_playlist, link=link )

    if __name__ == "__name__":
        app.run(debug=True)
