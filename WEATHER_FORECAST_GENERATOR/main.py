import os
import dotenv
import requests

dotenv.load_dotenv()

API_key = os.environ['API_KEY']
OWM_endpoint = os.environ['OWM_ENDPOINT']


def get_weather_data(city):
    weather_params = {
        "q": city.capitalize(),
        "units": "metric",
        "appid": API_key,
    }
    response = requests.get(url=OWM_endpoint, params=weather_params)
    response_status = response.status_code
    weather_data = response.json()

    if response_status == 200:
        data = {
            "description": weather_data['weather'][0]['description'],
            "temperature": weather_data['main']['temp'],
            "humidity": weather_data['main']['humidity'],
            "windspeed": weather_data['wind']['speed'],
        }
    else:
        data = {
            "description": "Invalid City Name"
        }

    return data