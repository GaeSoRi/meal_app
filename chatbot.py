from flask import Flask, request
import random
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    category = request.form['text']

    with open('data.json') as json_data:
        menus = json.load(json_data)
        categories = list(menus.keys())

    if category not in categories:
        category = random.choice(categories)

    food = random.choice(menus[category])

    res = {
        'response_type': 'in_channel',
        'text': f'{food}을(를) 먹는건 어때?'
    }

    return res

if __name__ == "__main__":
    app.run(port=1212, debug=True)
