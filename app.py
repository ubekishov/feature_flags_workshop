from flask import Flask, request, jsonify, render_template
import requests
import os
import json
import time
import random
from featureflags.client import CfClient
from featureflags.evaluations.auth_target import Target

ff_api_key = os.environ.get('FF_KEY')

app = Flask(__name__)
cf = CfClient(ff_api_key)

# Cache to store temperature values
temperature_cache = {}

OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY', None)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/temperature', methods=['GET'])
def get_temperature():
    city = request.args.get('city')
    units = request.args.get('units', 'metric')  # default to metric if not specified

    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    if request.headers.get('persona') == "tester":
        attributes = {
            "usertype": "internal",
            "company": "acme inc",
            "opted-into-beta": True
        }
        print("Tester!")
        target = Target(identifier="tester", name="tester", attributes=attributes)
    else:
        target = Target(identifier="user1", name="user1")

    if cf.bool_variation("cache_result", target, False):
        cache_key = f'{city}_{units}'  # The fix!
        if cache_key in temperature_cache:
            temperature = temperature_cache[cache_key]
            return jsonify({'city': city, 'temperature': temperature, 'units': units})

    try:
        if OPENWEATHER_API_KEY is not None:
            temperature = fetch_temperature(city, units)
        else:
            temperature = get_temperature_from_local(city, units)
        if cf.bool_variation("cache_result", target, False):
            temperature_cache[cache_key] = temperature
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


def get_temperature_from_local(city_name, units="imperial"):
    # Load city data from the JSON file
    with open("temperatures.json", "r") as file:
        cities_data = json.load(file)

    # Capitalize the first letter of each word in the city name
    formatted_city = ' '.join(word.capitalize() for word in city_name.split())

    delay = random.uniform(0.1, 0.6)
    time.sleep(delay)

    for city in cities_data["cities"]:
        if city["name"] == formatted_city:
            return city["temperature"][units]

    raise ValueError(f"City '{formatted_city}' not found in the list")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
