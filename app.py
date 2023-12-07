from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY')

if not OPENWEATHER_API_KEY:
    raise ValueError("OpenWeatherMap API key is not set. Please set the OPENWEATHER_API_KEY environment variable.")

@app.route('/temperature', methods=['GET'])
def get_temperature():
    city = request.args.get('city')
    units = request.args.get('units', 'metric')  # default to metric if not specified

    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    try:
        temperature = fetch_temperature(city, units)
        return jsonify({'city': city, 'temperature': temperature, 'units': units})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def fetch_temperature(city_name, units="imperial"):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city_name, 'units': units, 'appid': OPENWEATHER_API_KEY}

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp']
        return temperature
    else:
        error_message = data.get('message', 'Unknown error')
        raise Exception(f'Failed to fetch temperature: {error_message}')

def get_temperature(city_name, units="imperial"):
    # Load city data from the JSON file
    with open("cities_data.json", "r") as file:
        cities_data = json.load(file)

    # Capitalize the first letter of each word in the city name
    formatted_city = ' '.join(word.capitalize() for word in city_name.split())
    
    for city in cities_data["cities"]:
        if city["name"] == formatted_city:
            return city["temperature"][units]

    raise ValueError(f"City '{formatted_city}' not found in the list")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
