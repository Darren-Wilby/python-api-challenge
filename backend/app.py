import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from functions.rockPaperScissors import rock_paper_scissors
from functions.getRandomJoke import get_random_joke
from functions.getWeather import get_weather
from functions.getSynonyms import get_synonyms

app = Flask(__name__, static_folder='../react-frontend/build',
            static_url_path='/')

CORS(app)


# Serve static files from the React build directory
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    # If the requested path exists, serve the file, else serve index.html
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


# Handle POST requests to the root URL
@app.route('/', methods=['POST'])
def handle_request():
    try:
        data = request.get_json()
        command = data['command'].lower()
        name = data['name']

        # Handle different command cases
        if command == 'greeting':
            return {"response": f"hello {name}"}, 200
        elif command == 'life':
            return {"response": "...42"}, 200
        elif command in ['rock', 'paper', 'scissors']:
            computer_choice = rock_paper_scissors(command)
            return {"response": f"{computer_choice}, {name}"}, 200
        elif command == 'joke':
            joke = get_random_joke()
            return {"response": joke}, 200
        elif command.startswith('weather in '):
            city = command[11:]
            weather = get_weather(city)
            return {"response": weather}, 200
        elif command.startswith('synonyms for '):
            word = command[13:]
            synonyms = get_synonyms(word)
            return {"response": synonyms}, 200
        else:
            return {"response": f"I'm sorry, {name}, I'm afraid I can't do that"}, 403

    except Exception as e:
        print(str(e))
        return "Forbidden", 403


if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)
