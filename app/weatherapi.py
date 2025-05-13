import requests

API_KEY = ""
BASE_URL = "http://api.weatherapi.com/v1/forecast.json"

def get_weather_forecast(city, days):
    params = {
        "key": API_KEY,
        "q": city,
        "days": days,
        "aqi": "yes",
        "alerts": "yes"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        print(response)
        return response

        
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException


#get_weather_forecast("Gweru", 2)