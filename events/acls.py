import requests
import json
from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY


def get_city_photo(city, state):
    url = 'https://api.pexels.com/v1/search'
    query = {
        "query": f'{city} {state} skyline'
        }
    auth = {"Authorization": PEXELS_API_KEY}
    response = requests.get(url, headers=auth, params=query)

    content = json.loads(response.content)

    try:
        return {"picture_url": content["photos"][0]["src"]["original"]}
    except (KeyError, IndexError):
        return {"picture_url": None}


def get_weather(city, state):
    geo_params = {
        "q": f'{city},{state},US',
        "appid": OPEN_WEATHER_API_KEY
    }
    geo_url = 'http://api.openweathermap.org/geo/1.0/direct'
    geo_response = requests.get(geo_url, params=geo_params)
    geo_content = json.loads(geo_response.content)

    weather_params = {
        "lat": geo_content[0]['lat'],
        "lon": geo_content[0]['lon'],
        "units": "imperial",
        "appid": OPEN_WEATHER_API_KEY,
    }
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    weather_response = requests.get(weather_url, params=weather_params)
    weather_content = json.loads(weather_response.content)

    try:
        return {
                "temp": weather_content["main"]["temp"],
                "description": weather_content["weather"][0]["description"],
            }
    except (TypeError, IndexError):
        return {"weather": None}
