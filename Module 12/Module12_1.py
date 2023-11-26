import requests
from flask import Flask, request


def get_random_joke():
    api_url = "https://api.chucknorris.io/jokes/random"

    try:
        response = requests.get(api_url)
        response.raise_for_status()

        data = response.json()
        text = data["value"]

        return text
    except requests.RequestException as e:
        print(f"Error fetching Chuck Norris joke: {e}.")
        return None


if __name__ == "__main__":
    random_joke = get_random_joke()

    if random_joke:
        print("Chuck Norris Joke:")
        print(random_joke)



