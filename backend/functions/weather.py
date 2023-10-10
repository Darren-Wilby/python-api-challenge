import os
from dotenv import load_dotenv
import requests

load_dotenv()

def get_weather(city):
    api_key = os.getenv("API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city.replace(' ', '')}&appid={api_key}"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == 200:
        main_data = data["main"]
        weather_data = data["weather"][0]["description"]
        temp_kelvin = main_data["temp"]
        temp_celsius = temp_kelvin - 273.15

        return f"Weather in {city.capitalize()}: {weather_data}, Temperature: {temp_celsius:.1f}°C"
    else:
        return "City not found or an error occurred."