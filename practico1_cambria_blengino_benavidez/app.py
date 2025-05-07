import requests
from datetime import date

from flask import (
    Flask , 
    render_template,
    request,
)

app = Flask(__name__)





def get_ciudades():

    ciudades = {
    "Buenos Aires": {"lat": -34.6037, "lon": -58.3816},
    "Cordoba": {"lat": -31.4201, "lon": -64.1888},
    "Madrid": {"lat": 40.4168, "lon": -3.7038},
    "Nueva York": {"lat": 40.7128, "lon": -74.0060},
    "Tokio": {"lat": 35.6895, "lon": 139.6917},
    "Paris": {"lat": 48.8566, "lon": 2.3522},
    "Londres": {"lat": 51.5074, "lon": -0.1278},
    "Sidney": {"lat": -33.8688, "lon": 151.2093},
    "Ciudad de Mexico": {"lat": 19.4326, "lon": -99.1332},
    "El Cairo": {"lat": 30.0444, "lon": 31.2357}
    }

    return ciudades


def get_latitud_longitud(ciudad_pedida):
    ciudades = get_ciudades()
    latitud = 0
    longitud = 0
    ciudad_info = ciudades.get(ciudad_pedida)
    if ciudad_info:
        longitud = ciudad_info['lon']
        latitud = ciudad_info['lat']
    
    return latitud, longitud
        

        
    

@app.route("/")
def index():
  
    return render_template('index.html', ciudades = get_ciudades())

@app.route("/clima/")
def clima():
    ciudad = request.args.get("ciudad")
    latitud, longitud = get_latitud_longitud(ciudad_pedida=ciudad)
    response = requests.get(
        f'https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&current_weather=true'
    ).json()

    data = response['current_weather']

    return render_template('clima.html', data=data, ciudad=ciudad)

    