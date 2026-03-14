# Weather App - Docker Lab

A simple Python application that fetches weather data for any city and saves it to a JSON file.

## Project Structure

- `src/weather_app.py` - Main Python script
- `requirements.txt` - Python dependencies
- `Dockerfile` - Docker configuration

## Local Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run the script
python src/weather_app.py Boston
python src/weather_app.py "New York"
```

## Docker Setup

**Build the image:**
```bash
docker build -t weather-app .
```

**Run the container:**
```bash
# Default city (Boston)
docker run weather-app

# Custom city
docker run weather-app London
docker run weather-app "San Francisco"
```

**Extract output file:**
```bash
docker run --name weather-container weather-app Boston
docker cp weather-container:/app/weather_output.json .
docker rm weather-container
```

## Output

The app displays weather information and saves it to `weather_output.json`.