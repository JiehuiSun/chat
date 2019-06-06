#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-06-04 17:35:54
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.db import transaction
from .helpers import gen_roomname
from .models import Room, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.username = self.scope['url_route']['kwargs']['username']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
    # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # db
        with transaction.atomic():
            room_obj = Room.objects.filter(label=self.room_name).first()
            msg_obj = Message.objects.create(room_id=room_obj.id,
                                             message=message,
                                             handle=self.username)

        # Send message to room group
        msg = "{0} {1}: {2}".format(self.username,
                                    msg_obj.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                                    message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': msg
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
