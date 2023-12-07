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

def fetch_temperature(city, units):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'units': units, 'appid': OPENWEATHER_API_KEY}

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp']
        return temperature
    else:
        error_message = data.get('message', 'Unknown error')
        raise Exception(f'Failed to fetch temperature: {error_message}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
