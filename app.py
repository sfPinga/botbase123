# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 01:00:17 2018

@author: linzino
"""


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('K+drqF7fD60Umv0MJcWZCipkDqUQvBpfHJjVVqpLXLiFEqdujEFH+uNAi3oFHqladenozrOPxycVQYjryiysqQrnRRH8av8yZTiJpOTVss+UD7HBW6b3JUu2mWAp2s/i5WY9DHmjkcLE1eB/+R+BVwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9f48c2c5098e03a82a51f9fae03bfda7')



@app.route("/callback", methods=['POST'])
def callback():

    
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
 

print('juhuhu')

if __name__ == '__main__':
    app.run(debug=True)


for i in range(0,10):
    print(i)