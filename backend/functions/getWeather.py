import os
from dotenv import load_dotenv
import requests

load_dotenv()


def get_weather(city):
    """
    Get the weather information for a specific city.

    Args:
        city (str): The name of the city for which weather information is requested.

    Returns:
        str: A string describing the weather conditions and temperature for the specified city.
             Returns an error message if the city is not found or an error occurs during the request.
    """
    api_key = os.getenv("WEATHER_API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city.replace(' ', '')}&appid={api_key}"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == 200:
        main_data = data["main"]
        weather_data = data["weather"][0]["description"]
        temp_kelvin = main_data["temp"]
        temp_celsius = temp_kelvin - 273.15

        return f"Weather in {city.title()}: {weather_data}, Temperature: {temp_celsius:.1f}°C"
    else:
        return "City not found or an error occurred."
