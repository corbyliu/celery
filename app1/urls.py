#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 下午5:56
# @Author  : liuss
# @Email   : liuss@udsafe.com.cn
# @File    : urls.py

from django.urls import path
from app1.views import TestView

urlpatterns = [
    path("celery/", TestView.as_view())
]
