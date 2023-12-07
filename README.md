# Weather API

This is a simple Flask application that provides an API endpoint to fetch the temperature of a city from OpenWeatherMap. The application can be Dockerized for easy deployment.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/) (>= 3.8)
- [Docker](https://www.docker.com/)

### Installation

```bash
git clone https://github.com/yourusername/weather-api.git
```

#### OpenWeatherMap API Key
1. Visit OpenWeatherMap and sign up for an account.
2. Obtain your API key from the dashboard.

#### Build and Run
```bash
docker build -t weather-api .
docker run -p 5000:5000 -e OPENWEATHER_API_KEY=<your_openweather_api_key> weather-api
```
Replace <your_openweather_api_key> with your actual OpenWeatherMap API key.


### Usage
Access the API endpoint at http://localhost:5000/temperature.

#### API Endpoint
* Endpoint: /temperature
* Method: GET
* Parameters:
* * city (required): Name of the city.
* * units (optional): Temperature units (imperial or metric). Defaults to metric.
##### Example Request:
```bash
curl http://localhost:5000/temperature?city=London&units=metric
```
##### Example Response:
```json
{
  "city": "London",
  "temperature": 20.5,
  "units": "metric"
}
```

## Testing the API with the provided script

### Running the Test Script

To test your Weather API endpoint with the provided script, use the following command:

```bash
python test_script.py --endpoint http://your-api-endpoint/temperature # This will default to localhost if you don't specify, so only add if necessary
```

### Example Output
```
City           Metric    Imperial
New York       20.30     68.50
Los Angeles    24.00     75.20
Houston        26.70     80.10
London         14.90     58.90
Hong Kong      25.60     78.10
```

