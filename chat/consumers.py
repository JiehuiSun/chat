#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-06-04 13:50:58
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: consumers.py

from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print("*" * 40)
        self.accept()

    def disconnect(self, close_code):
        print("-" * 40)
        pass

    def receive(self, text_data):
        print("=" * 40)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
