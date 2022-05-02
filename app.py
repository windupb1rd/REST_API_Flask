from flask import Flask, request, jsonify, abort
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/api/questions', methods=['POST'])
def get_question():
    if request.json and 'questions_num' in request.json:
        questions_num = request.json['questions_num']
        response_from_api = requests.get(f'https://jservice.io/api/random?count={questions_num}').json()

        res = {}
        for index, question in enumerate(response_from_api):
            res[index] = question

    else:
        abort(400)

    return res


if __name__ == '__main__':
    app.run(debug=True)
