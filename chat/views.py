#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-06-04 11:48:52
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: views.py


import json
from django.shortcuts import render, HttpResponse
from django.utils.safestring import mark_safe
from django.db import transaction
from .models import Room, Message
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

    room_obj = None
    with transaction.atomic():
        if not Room.objects.filter(label=room_name).exists():
            label = gen_roomname(room_name)
            room_obj = Room.objects.create(name=room_name, label=label)
            room_name = label
    if not room_obj:
        room_obj = Room.objects.filter(label=room_name).first()
    msg_obj_list = Message.objects.filter(room_id=room_obj.id).all()
    msg_list = [i.message for i in msg_obj_list]
    return render(request, 'chat/room.html', {
                'room_name': mark_safe(json.dumps(room_name)),
                'room_msg': mark_safe(msg_list)
            })


def login(request):
    return render(request, "chat/login.html", {})


def user_login(request):
    ret = {"code": 0}
    params = request.POST
    if not params:
        ret["code"] = 1
    elif not params.get("username") or not params.get("password"):
        ret["code"] = 2
    return HttpResponse(json.dumps(ret, ensure_ascii=False), content_type = "application/json")
