import requests
import os
from dotenv import load_dotenv
import re

def is_valid_city(city_name):
    """Check if city name is valid."""
    return re.match(r'^[A-Za-z]+(?:[\s-][A-Za-z]+)*$', city_name) is not None

def get_weather_data(city_name, api_key):
    """Get weather data from WeatherAPI"""
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no'
    # Make API request
    try:
        response = requests.get(url)
        # Return JSON data
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        return print(f"Error in API request.")

def print_weather_data(data):
    """Print weather data."""
    # Get weather data
    location = data['location']['name']
    country = data['location']['country']
    temperature = data['current']['temp_c']
    humidity = data['current']['humidity']
    condition = data['current']['condition']['text']
    wind_speed = data['current']['wind_kph']
    pressure = data['current']['pressure_mb']
    precip_mm = data['current']['precip_mm']
    visibility = data['current']['vis_km']
    
    # Print weather data
    print(f'\033[1mWeather\033[0m in {location}, {country}:')
    print(f'\033[1mTemperature\033[0m: {temperature}°C')
    print(f'\033[1mHumidity\033[0m: {humidity}%')
    print(f'\033[1mCondition\033[0m: {condition}')
    print(f'\033[1mWind Speed\033[0m: {wind_speed} km/h')
    print(f'\033[1mPressure\033[0m: {pressure} mBar')
    print(f'\033[1mPrecipitation\033[0m: {precip_mm} mm')
    print(f'\033[1mVisibility\033[0m: {visibility} km')

def main():
    # Load API key from environment file
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    city = input("Enter the city name: ")
    # Check if city name is valid
    if not is_valid_city(city):
        print("Invalid city name.")
        return
    # Get weather data
    data = get_weather_data(city, API_KEY)
    if data is None:
        print("Error in API request.")
    else:
        print_weather_data(data)

if __name__ == "__main__":
    main()