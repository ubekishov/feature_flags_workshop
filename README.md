# Weather API

This is a simple Flask application that provides an API endpoint to fetch the temperature of a city from OpenWeatherMap. The application can be Dockerized for easy deployment.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/) (>= 3.8)
- [Docker](https://www.docker.com/)

### Installation

```bash
git clone https://github.com/yourusername/weather-api.git
cd weather-api
pip install -r requirements.txt
```

### OpenWeatherMap API Key
1. Visit OpenWeatherMap and sign up for an account.
2. Obtain your API key from the dashboard.

#### Build and Run
```bash
docker build -t weather-api .
docker run -p 5000:5000 -e OPENWEATHER_API_KEY=<your_openweather_api_key> weather-api
```
Replace <your_openweather_api_key> with your actual OpenWeatherMap API key.

