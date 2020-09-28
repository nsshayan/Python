"""
A simple program to fetch weather report for a city
(defaults to 'Bengaluru') using OpenWeatherMap API

"""

API_KEY = "932c152d6ff8d185bfdd9d2a5f8e33e4"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

Output = """
Location:            {}
Description:         {}
Current temperature: {}\u00B0 Celsius
Minimum temperature: {}\u00B0 Celsius
Maximum temperature: {}\u00B0 Celsius
Sunrise at:          {}
Sunset at:           {}
"""


def get_weather_report(location):
    import requests
    QUERY_STRING = f"?q={location}&units=metric&APPID={API_KEY}"
    URL = BASE_URL + QUERY_STRING

    response = requests.get(URL)
    if response.ok:
        result = response.json()
        return Output.format(
            location,
            result["weather"][0]["description"].capitalize(),
            result["main"]["temp"],
            result["main"]["temp_min"],
            result["main"]["temp_max"],
            result["sys"]["sunrise"],
            result["sys"]["sunset"]
        )


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "location",
        nargs='?', const="Bengaluru",
        help="get weather report for a location")

    args = parser.parse_args()

    results = get_weather_report(args.location)
