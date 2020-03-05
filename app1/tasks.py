#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 下午5:48
# @Author  : liuss
# @Email   : liuss@udsafe.com.cn
# @File    : tasks.py

from __future__ import absolute_import
from celery import shared_task
import time


@shared_task
def add(x, y):
    time.sleep(10)
    print("running...", x, y)
    return x + y
