import requests


def get_weather(city):
    api_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = 'd565e6b52d9a7f6a916b68b4b7883be7'
    params = {
        'q': city,
        'appid': api_key,
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()

        data = response.json()

        description = data['weather'][0]['description']
        temperature_kelvin = data['main']['temp']

        temperature_celsius = temperature_kelvin -273.15

        return description, temperature_celsius
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}.")
        return None


if __name__ == "__main__":
    city = input("Enter the name of the city: ")
    description, temperature = get_weather(city)
    if description is not None and temperature is not None:
        print(f"Weather in {city}: {description}")
        print(f"Temperature: {temperature:.2f} °C")
