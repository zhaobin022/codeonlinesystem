#-*- coding: UTF-8 -*-
from django.shortcuts import HttpResponse


def _auth(args):  # args 是传入的，需要验证的权限
    def __auth(func):
        def _login(request):
            if args == 'admin':
                return func(request)  # 权限验证通过，继续执行视图
            else:
                return HttpResponse('deny ')  # 否则执行禁止视图
        return _login
    return __auth
