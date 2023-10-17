import requests

JOKES_API_ENDPOINT = 'https://v2.jokeapi.dev/joke/Any'


def get_random_joke():
    response = requests.get(JOKES_API_ENDPOINT)
    if response.status_code == 200:
        data = response.json()
        if data['type'] == 'single':
            return data['joke']
        elif data['type'] == 'twopart':
            return f"{data['setup']} {data['delivery']}"
    return "Joke not found or error occurred."
