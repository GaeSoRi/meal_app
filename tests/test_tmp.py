from meal_app import chatbot
app = chatbot.app.test_client()

def test_get_food():
    res = app.post('/', data={'text': ''}, content_type='multipart/form-data')
    assert res.status_code == 200

def test_get_food_text_value():
    res = app.post('/', data={'text': '한식'}, content_type='multipart/form-data')
    assert res.status_code == 200

def test_get_food_text_non_exist_value():
    res = app.post('/', data={'text': '가나다'}, content_type='multipart/form-data')
    assert res.status_code == 200