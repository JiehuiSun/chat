#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-06-04 13:52:20
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: routing.py


from django.conf.urls import url
# from django.urls import path

from . import consumers

websocket_urlpatterns = [
    url('ws/chat/(?P<room_name>\w+)/(?P<username>\w+)$', consumers.ChatConsumer),
    # path('ws/chat/<str:room_name>)/$', consumers.ChatConsumera),
]
