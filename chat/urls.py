#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-06-04 11:47:52
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.index, name='index'),
]
