# WeatherAPI Python Script

This script allows you to retrieve the current weather information for a given city using the WeatherAPI.

### Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)
- `dotenv` library (`pip install python-dotenv`)

### Usage

1. Make sure you have registered for an API key at [WeatherAPI](https://www.weatherapi.com/) and stored it in a `.env` file in the same directory as this script, under the variable `API_KEY`.

2. Run the script by executing the following command in your terminal:

   ```shell
   python3 weather.py
   ```
3. Enter the name of the city for which you want to retrieve the weather information when prompted.

### Example
Enter the city name: Palermo
- **Weather** in Palermo, Italy:
- **Temperature**: 11.0°C
- **Humidity**: 66%
- **Condition**: Light rain
- **Wind Speed**: 25.9 km/h
- **Pressure**: 1008.0 mBar
- **Precipitation**: 0.11 mm
- **Visibility**: 10.0 km