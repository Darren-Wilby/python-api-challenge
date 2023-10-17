import os
from dotenv import load_dotenv
import requests

load_dotenv()

WORDS_API_KEY = os.getenv('WORDS_API_KEY')
WORDS_API_ENDPOINT = 'https://wordsapiv1.p.rapidapi.com/words/'

headers = {
    'X-RapidAPI-Host': 'wordsapiv1.p.rapidapi.com',
    'X-RapidAPI-Key': WORDS_API_KEY
}


def get_synonyms(word):
    response = requests.get(
        f'{WORDS_API_ENDPOINT}{word}/synonyms', headers=headers)
    if response.status_code == 200:
        data = response.json()
        return f"Synonyms: {', '.join([synonym for synonym in data['synonyms']])}"
    else:
        return "Word not found or an error occurred."
