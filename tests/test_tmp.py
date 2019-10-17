from gsr_meal_chatbot import chatbot
app = chatbot.app.test_client()

def test_get_food():
    res = app.post('/', data={'text': '한식'}, content_type='multipart/form-data')
    assert res.status_code == 200