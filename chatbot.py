from flask import Flask, request
import random

app = Flask(__name__)

categories = ['한식', '일식', '중식', '양식']
menus = {'한식': ['국밥', '갈비탕', '냉면', '치킨', '해장국', '순두부찌개', '김치찌개', '부대찌개', '떡볶이', '비빔밥', '된장', '감자탕', '칼국수', '설렁탕', '보쌈', '김원준'],
         '일식': ['우동', '규동', '소바', '라멘', '카레', '돈까스', '오므라이스', '햄버그 스테이크'],
         '중식': ['짜장면', '짬뽕', '볶음밥', '마라탕', '마라샹궈', '기스면', '깐풍기', '탕수육', '소룡포', '우육면'],
         '양식': ['돈까스', '피자', '햄버거', '스파게티', '타코']}

@app.route('/', methods=['POST'])
def index():
    category = request.form['text']

    if not category or category not in categories:
        category = random.choice(categories)

    food = random.choice(menus[category])

    res = {
        'response_type': 'in_channel',
        'text': f'{food}을(를) 먹는건 어때?'
    }

    return res

if __name__ == "__main__":
    app.run(port=1212)
