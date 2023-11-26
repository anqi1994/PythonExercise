import requests


def get_weather(api_key, city):
    api_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'appid': api_key,
        'q': city,
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()

        data = response.json()

        description = data['weather'][0]['description']
        temperature_k = data['main']['temp']
        temperature_c = round(temperature_k - 273.15, 2)

        print(description, temperature_c)
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}.")

        return None, None


name = "__main__"
api_key = input("Enter your api key: ")
city = input("Enter the name of the city: ")
get_weather(api_key, city)



