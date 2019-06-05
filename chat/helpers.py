#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-06-05 13:54:00
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: helpers.py


import time
import hashlib


def gen_roomname(room_name):
    """
    """
    roomname = hashlib.sha256(str("{0}{1}".format(str(room_name), str(time.time()))).encode("utf8")).hexdigest()
    return roomname
