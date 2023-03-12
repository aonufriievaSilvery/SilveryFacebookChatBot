from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)

# Введите данные для подключения к Facebook API
ACCESS_TOKEN = 'EAAhyecWdfRQBAN6OeulEgBwAZB59MpbhudoDQasnoZCk3txwyamvv8mMcuDnDDH8yOqCSL78pD29LHis15jUuet2Cc0y0dm4eup5ALmJZA7ZAtZBs2nZBrHkNiB7RNzeWQLEBS9GzXfICqENvaYheArWDGMKDYy7ggnl6MZCLswewc9oXhAlTMG'
# VERIFY_TOKEN = 'MDAhyecWdfRQBAN6OeulEgBwAZB59MpbhudoDQasnoZCk3txwyamvv8mMcuDnDDH8yOqCSL78pD29LHis15jUuet2Cc0y0dm4eup5ALmJZA7ZAtZBs2nZBrHkNiB7RNzeWQLEBS9GzXfICqENvaYheArWDGMKDYy7ggnl6MZCLswewc9oXhAlTMG'
VERIFY_TOKEN = '7A12801B674BA3DAEDB27E00B5D268EF6656FA3A19355E6CCCBC75E43D31A40E'

bot = Bot(ACCESS_TOKEN)

# Функция для создания кнопок
def create_button(title, payload):
    return {
        "type": "postback",
        "title": title,
        "payload": payload
    }

# Функция для отправки сообщения с кнопками
def send_message(recipient_id, message, buttons=None):
    button_list = None
    if buttons:
        button_list = [create_button(title, payload) for title, payload in buttons.items()]
    bot.send_button_message(recipient_id, message, button_list)

# Обработчик входящих сообщений
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                if messaging_event.get('message'):
                    sender_id = messaging_event['sender']['id']
                    message_text = messaging_event['message']['text']
                    send_message(sender_id, 'Вы написали: {}'.format(message_text), buttons={
                        'Кнопка 1': 'payload_1',
                        'Кнопка 2': 'payload_2'
                    })
    return "ok"

if __name__ == '__main__':
    app.run(debug=True)
