#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 下午5:13
# @Author  : liuss
# @Email   : liuss@udsafe.com.cn
# @File    : celery.py


from __future__ import absolute_import, unicode_literals
import os
from datetime import timedelta
from django.conf import settings
from celery import Celery
from celery.schedules import crontab

# 设置 Django 的配置文件
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_test.settings')
# 创建 celery 实例
app = Celery("celery_test", broker='redis://127.0.0.1:6379/1', backend='redis://127.0.0.1:6379/2')

app.config_from_object('django.conf:settings', namespace='CELERY')
# 搜索所有 app 中的 tasks
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


app.conf.beat_schedule = {
    "each3m_task": {
        "task": "app1.tasks.add",
        "schedule": crontab(minute=16),
        "args": (2, 4)
    },
    "each4m_task": {
        "task": "app1.tasks.add",
        "schedule": timedelta(seconds=10),
        "args": (3, 7)
    }
}

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=2
)
