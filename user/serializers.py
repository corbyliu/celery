#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 下午9:22
# @Author  : liuss
# @Email   : liuss@udsafe.com.cn
# @File    : serializers.py

from rest_framework import serializers
from user import models


class LodinUserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ('id', 'username', 'phone', 'email')
