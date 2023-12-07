import requests
import argparse


def query_temperature(endpoint, city, units):
    response = requests.get(endpoint, params={'city': city, 'units': units})
    data = response.json()

    if response.status_code == 200:
        return data['temperature'], units
    else:
        return f"Error: {data.get('error', 'Unknown error')}", units


def main():
    parser = argparse.ArgumentParser(description="Query temperature endpoint for cities in metric and imperial units.")
    parser.add_argument(
        '--endpoint',
        default='http://localhost:5000/temperature',
        help='Endpoint URL for temperature query'
    )
    args = parser.parse_args()

    cities = ["New York", "Los Angeles", "Houston", "London", "Hong Kong"]

    # Print header
    print(f"{'City':<15}{'Metric':<10}{'Imperial':<10}")

    # Query temperatures for each city
    for city in cities:
        metric_temp, _ = query_temperature(args.endpoint, city, units="metric")
        imperial_temp, _ = query_temperature(args.endpoint, city, units="imperial")
        
        print(f"{city.capitalize():<15}{metric_temp:<10.2f}{imperial_temp:<10.2f}")


if __name__ == "__main__":
    main()

