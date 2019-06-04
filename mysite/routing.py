#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-06-04 11:53:57
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: routing.py

from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter({
    # (http->django views is added by default)
})
