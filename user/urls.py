#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 下午9:29
# @Author  : liuss
# @Email   : liuss@udsafe.com.cn
# @File    : urls.py

from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from user import views

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('manager/', views.CreateUser.as_view()),
]
