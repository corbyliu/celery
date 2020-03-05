#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 下午9:11
# @Author  : liuss
# @Email   : liuss@udsafe.com.cn
# @File    : utils.py

from django.contrib.auth.backends import ModelBackend
import re
from user import models


class UserPhoneEmailAuthBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        """

        :param request:
        :param username:可能是手机号码/邮箱/用户名
        :param password:
        :param kwargs:
        :return:
        """
        # 1.　todo 不管是用户或者邮箱或者手机号码，第一件事获取对象
        try:
            # todo 先通过正则，判断出手机号码/用户名/邮箱
            if re.match(r'^1[\d]{10}$', username):
                user = models.User.objects.get(phone=username)
                print('111111111111111111eeeeeeeeerrrrrrrrrrrrrrrrr')
            elif re.match('^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,4}$', username):
                user = models.User.objects.get(email=username)
            else:
                user = models.User.objects.get(username=username)

        except models.User.DoesNotExist:
            user = None

            # todo 拿到user之后进行校验
        if user is not None and user.check_password(password):
            return user


def jwt_response_username_userid_token(token, user=None, request=None):
    """

    :param token:
    :param user:
    :param request:
    :return:
    """
    data = {
        "token": token,
        "username": user.username,
        "user_id": user.id
    }
    return data
