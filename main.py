from urllib import request
from pymessenger.bot import Bot

ACCESS_TOKEN = 'EAAhyecWdfRQBAN6OeulEgBwAZB59MpbhudoDQasnoZCk3txwyamvv8mMcuDnDDH8yOqCSL78pD29LHis15jUuet2Cc0y0dm4eup5ALmJZA7ZAtZBs2nZBrHkNiB7RNzeWQLEBS9GzXfICqENvaYheArWDGMKDYy7ggnl6MZCLswewc9oXhAlTMG'
VERIFY_TOKEN = 'MDAhyecWdfRQBAN6OeulEgBwAZB59MpbhudoDQasnoZCk3txwyamvv8mMcuDnDDH8yOqCSL78pD29LHis15jUuet2Cc0y0dm4eup5ALmJZA7ZAtZBs2nZBrHkNiB7RNzeWQLEBS9GzXfICqENvaYheArWDGMKDYy7ggnl6MZCLswewc9oXhAlTMG'
bot = Bot(ACCESS_TOKEN)

# Функция для обработки запроса от пользователя
def process_message(message):
    # Ваш код для обработки сообщения
    return "Hello, World!"

# Функция для отправки сообщения пользователю с кнопками меню
def send_menu(recipient_id):
    button_list = [
        {
            "type": "postback",
            "title": "Button 1",
            "payload": "Payload for button 1"
        },
        {
            "type": "postback",
            "title": "Button 2",
            "payload": "Payload for button 2"
        }
    ]
    bot.send_button_message(recipient_id, "Choose an option:", button_list)

# Функция для отправки сообщения пользователю
def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)

# Функция для проверки токена подтверждения
def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

# Функция для обработки входящих сообщений от пользователей
def receive_message(request):
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        if message['message']['text'] == 'menu':
                            send_menu(recipient_id)
                        else:
                            response_sent_text = process_message(message['message']['text'])
                            send_message(recipient_id, response_sent_text)
                elif message.get('postback'):
                    payload = message['postback']['payload']
                    send_message(recipient_id, "You clicked " + payload)
        return "Message Processed"
