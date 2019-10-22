from flask import Blueprint, request

from app.services.meal import get_food

meal_bp =  Blueprint('meal_bp', __name__)

@meal_bp.route('', methods=['POST'])
def meal():
    category = request.form['text']
    food = get_food(category)

    return {
        'response_type': 'in_channel',
        'text': f'{food}을(를) 먹는건 어때?'
    }
