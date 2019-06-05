#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-06-04 18:08:42
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: models.py

from django.db import models
from django.utils import timezone

class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
