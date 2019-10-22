# from meal_app import chatbot
from meal_app.app.services.meal import get_food

import json

# app = chatbot.app.test_client()

with open('data.json') as json_data:
    menus = json.load(json_data)

# def extract_food_from_text(text):
#     if text.find('을') > text.find('를'):
#         food = text[:text.find('를')]
#     else:
#         food = text[:text.find('을')]
    
#     return food

# def test_get_food():
#     res = app.post('/api/v1/meal', data={'text': ''}, content_type='multipart/form-data')
#     food = extract_food_from_text(json.loads(res.data)['text'])
#     foods = []

#     for i in menus:
#         foods.extend(menus[i])

#     assert res.status_code == 200
#     assert food in foods

# def test_get_food_text_value():
#     res = app.post('/api/v1/meal', data={'text': '한식'}, content_type='multipart/form-data')
#     food = extract_food_from_text(json.loads(res.data)['text'])

#     assert res.status_code == 200
#     assert food in menus['한식']

# def test_get_food_text_non_exist_value():
#     res = app.post('/api/v1/meal', data={'text': '가나다'}, content_type='multipart/form-data')
#     food = extract_food_from_text(json.loads(res.data)['text'])
#     foods = []

#     for i in menus:
#         foods.extend(menus[i])

#     assert res.status_code == 200
#     assert food in foods

def test_get_food_한식():
    food = get_food('한식')

    assert food in menus['한식']

def test_get_food_with_non_exist_category():
    food = get_food('가나다')

    foods = []

    for i in menus:
        foods.extend(menus[i])

    assert food in foods

