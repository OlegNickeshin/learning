# WeatherFetcher (CLI)

A simple command-line tool to fetch current weather by city name using Open-Meteo and Nominatim APIs.

## 🔧 Requirements

- Python **3.7+** (tested on 3.12)
- `requests`
- `requests-cache`
- `retry-requests`

Install dependencies with:

```bash
pip install -r requirements.txt
```

🚀 Usage

```bash
python weather_fetcher.py --city "Moscow" --units metric
```

## Arguments

    --city (required): Name of the city (e.g., "Berlin", "Tokyo")

    --units: Choose between metric (°C) or imperial (°F). Default is metric.

## 🌐 Example Output

Moscow: 23.1°C
