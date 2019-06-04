#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-06-04 11:48:52
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: views.py


from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
                'room_name_json': mark_safe(json.dumps(room_name))
            })
