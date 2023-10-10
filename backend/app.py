import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from functions.rockPaperScissors import rock_paper_scissors
from functions.randomJoke import random_joke
from functions.weather import get_weather

app = Flask(__name__, static_folder='../react-frontend/build')
CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


@app.route('/', methods=['POST'])
def handle_request():
    try:
        data = request.get_json()
        command = data['command'].lower()
        name = data['name']

        if command == 'greeting':
            response = {"response": f"hello {name}"}
        elif command == 'what is the meaning of life':
            response = {"response": f"the meaning of life is...42"}
        elif command in ['rock', 'paper', 'scissors']:
            computer_choice = rock_paper_scissors(command)
            response = {"response": computer_choice}
        elif command == 'tell me a joke':
            joke = random_joke()
            response = {"response": joke}
        elif command.startswith('what is the weather like in '):
            city = command[28:]
            weather = get_weather(city)
            response = {"response": weather}
        else:
            response = {"response": f"I'm sorry, {name}, I'm afraid I can't do that"}
            return jsonify(response), 403
        return jsonify(response), 200

    except Exception as e:
        print(str(e))
        return "Forbidden", 403

if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)
