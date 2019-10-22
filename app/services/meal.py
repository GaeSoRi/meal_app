import json
import random

def get_food(category):
    with open('data.json') as json_data:
        menus = json.load(json_data)
        categories = list(menus.keys())

    if category not in categories:
        category = random.choice(categories)

    return random.choice(menus[category])
