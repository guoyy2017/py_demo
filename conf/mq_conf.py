#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/3.下午4:34
'''

'''
rabbitmq 配置
'''

DEV={
    'db_host':'dev',
    'db_port':5672,
    'db_user':'dev',
    'db_passwd':'dev',
    'db_virtual_host':'/',
}

TEST={
    'db_host':'test',
    'db_port':5672,
    'db_user':'test',
    'db_passwd':'test',
    'db_virtual_host':'/',
}

PROD={
    'db_host':'prod',
    'db_port':5672,
    'db_user':'prod',
    'db_passwd':'prod',
    'db_virtual_host':'/',
}

if __name__ == '__main__':
    pass