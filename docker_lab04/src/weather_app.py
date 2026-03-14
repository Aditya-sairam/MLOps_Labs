import requests 
import json 
from datetime import datetime 
import sys

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"


    try:
        response = requests.get(url,timeout=10)
        response.raise_for_status() 
        data = response.json() 

        current = data['current_condition'][0]
        weather_info = {
            'city': city,
            'temperature_f': current['temp_F'],
            'temperature_c': current['temp_C'],
            'condition': current['weatherDesc'][0]['value'],
            'humidity': current['humidity'],
            'wind_speed': current['windspeedMiles'],
            'timestamp': datetime.now().isoformat()
        }
        return weather_info 
    except Exception as e:
        print(f"An error occured while fetching the weather..")
        return None 
    
def save_to_file(weather_data,filename='weather_output.json'):
    with open(filename,'w') as f:
        json.dump(weather_data,f,indent=2)
    print("Weather data saved to a file successfully")

def display_weather(weather_data):
    if weather_data:
        print(f"\n{'='*50}")
        print(f"Weather in {weather_data['city']}")
        print(f"{'='*50}")
        print(f"Temperature: {weather_data['temperature_f']}°F / {weather_data['temperature_c']}°C")
        print(f"Condition: {weather_data['condition']}")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']} mph")
        print(f"{'='*50}\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python weather_app.py <city_name>")
        sys.exit(1)

    city = " ".join(sys.argv[1:])
    print(f"Fetching weather for {city}...")
    weather_data = get_weather(city)
    print(weather_data)
    if weather_data:
        display_weather(weather_data)
        save_to_file(weather_data)
    else:
        print("Failed to fetch weather data.")
        sys.exit(1)