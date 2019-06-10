#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-06-04 11:47:52
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
    # url('<str:room_name>/', views.room, name='room'),
    url(r'^image/(?P<filename>\w+)', views.image, name='image'),
    url(r'^user_login', views.user_login, name='user_login'),
    url(r'^login', views.login, name='login'),
    url('(?P<room_name>\w+)/(?P<username>\w+)', views.room, name='room'),
    url('^$', views.index, name='index'),
    url(r'^upload', views.upload, name='upload'),
]
