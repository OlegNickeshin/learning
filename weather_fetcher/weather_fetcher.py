import requests
import argparse
import requests_cache
from retry_requests import retry

class WeatherFetcher: 
    def __init__(self, city, units='metric'):
        self.city = city
        self.units = units
        self.lat = None
        self.lon = None
        self.temp = None

    def geocode_with_details(self):
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": self.city,
            "format": "json",
            "limit": 1,
            "addressdetails": 1,
        }
        headers = {"User-Agent": "weather-fetcher-script"}
        try:
            resp = requests.get(url, params=params, headers=headers, timeout=5)
            data = resp.json()
            if data:
                self.lat = float(data[0]['lat'])
                self.lon = float(data[0]['lon'])
        except Exception as e:
            print(f"Geocoding failed: {e}")

    def open_meteo(self):
        if self.lat and self.lon:
            url = "https://api.open-meteo.com/v1/forecast"
            unit_param = "fahrenheit" if self.units == "imperial" else "celsius"
            params = {
                "latitude": self.lat,
                "longitude": self.lon,
                "current_weather": True,
                "temperature_unit": unit_param
            }

            try:
                # optional: cache session to avoid rate limits
                session = requests_cache.CachedSession('.cache', expire_after=3600)
                retry_session = retry(session, retries=3, backoff_factor=0.3)
                resp = retry_session.get(url, params=params, timeout=5)
                data = resp.json()
                self.temp = data["current_weather"]["temperature"]
            except Exception as e:
                print(f"Weather fetch failed: {e}")

    def show_weather(self):
        if self.temp is not None:
            symbol = "°F" if self.units == "imperial" else "°C"
            print(f"{self.city}: {self.temp}{symbol}")
        else:
            print("Weather data not available.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='City Weather Fetcher')
    parser.add_argument('--city', type=str, required=True, help='Enter the name of a city')
    parser.add_argument('--units', type=str, choices=['metric', 'imperial'], default='metric',
                        help='Use metric (°C) or imperial (°F) units')
    args = parser.parse_args()

    wf = WeatherFetcher(args.city, args.units)
    wf.geocode_with_details()
    wf.open_meteo()
    wf.show_weather()
