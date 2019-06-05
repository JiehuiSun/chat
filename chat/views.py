#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-06-04 11:48:52
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: views.py


import json
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.db import transaction
from .models import Room
from .helpers import gen_roomname

def index(request):
    room_obj_list = Room.objects.all()
    room_list = [
        {
            "room_name": i.name,
            "label": i.label
        } for i in room_obj_list
    ]

    return render(request, 'chat/index.html', {"room_list": room_list})


def room(request, room_name):
    if not room_name:
        return render(request, "chat/index.html", {})

    with transaction.atomic():
        label = gen_roomname(room_name)
        if not Room.objects.filter(label=label).exists():
            new_room = Room.objects.create(name=room_name, label=label)
    return render(request, 'chat/room.html', {
                'room_name_json': mark_safe(json.dumps(label))
            })

