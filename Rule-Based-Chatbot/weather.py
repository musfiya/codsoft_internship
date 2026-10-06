
import requests


def get_weather(city):
    """
    Fetch current weather information for a city
    using Open-Meteo's geocoding and weather APIs.
    """

    try:
        # -----------------------------
        # 1. Find the city coordinates
        # -----------------------------
        geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"

        geocoding_params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        location_response = requests.get(
            geocoding_url,
            params=geocoding_params,
            timeout=10
        )

        location_response.raise_for_status()

        location_data = location_response.json()

        if not location_data.get("results"):
            return f"I couldn't find a location called {city}."

        location = location_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]
        location_name = location["name"]

        # -----------------------------
        # 2. Get current weather
        # -----------------------------
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,"
                "relative_humidity_2m,"
                "weather_code,"
                "wind_speed_10m"
            ),
            "temperature_unit": "celsius",
            "wind_speed_unit": "kmh"
        }

        weather_response = requests.get(
            weather_url,
            params=weather_params,
            timeout=10
        )

        weather_response.raise_for_status()

        weather_data = weather_response.json()

        current = weather_data.get("current")

        if not current:
            return "Weather data is currently unavailable."

        temperature = current.get("temperature_2m")
        humidity = current.get("relative_humidity_2m")
        wind_speed = current.get("wind_speed_10m")
        weather_code = current.get("weather_code")

        condition = get_weather_condition(weather_code)

        return (
            f"Current weather in {location_name}:\n"
            f"Temperature: {temperature}°C\n"
            f"Condition: {condition}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} km/h"
        )

    except requests.exceptions.RequestException as error:
        print(f"Weather API error: {error}")

        return (
            "I'm unable to access the weather service right now. "
            "Please try again later."
        )

    except Exception as error:
        print(f"Weather processing error: {error}")

        return (
            "Something went wrong while retrieving the weather information."
        )


def get_weather_condition(code):
    """
    Convert Open-Meteo weather codes into readable conditions.
    """

    if code == 0:
        return "Clear sky"

    elif code in [1, 2, 3]:
        return "Partly cloudy"

    elif code in [45, 48]:
        return "Foggy"

    elif code in [51, 53, 55]:
        return "Drizzle"

    elif code in [61, 63, 65]:
        return "Rain"

    elif code in [71, 73, 75]:
        return "Snow"

    elif code in [80, 81, 82]:
        return "Rain showers"

    elif code in [95, 96, 99]:
        return "Thunderstorm"

    else:
        return "Unknown weather condition"
