#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/2.下午3:56
'''

import os
import my_except

#APP 名称
APP_NAME = 'DEMO'
DEFAULT = 'DEV'
#运行环境 默认DEV 开发
run_evn = os.getenv(APP_NAME, DEFAULT)

def get_mysql_conf():
    '''
    获取mysql 配置
    :return:
    '''
    from conf import mysql_conf
    if hasattr(mysql_conf, run_evn):
        return getattr(mysql_conf,run_evn)
    else:
        raise my_except.ConfError()

def get_redis_conf():
    '''
    获取redis 配置
    :return:
    '''
    from conf import redis_conf
    if hasattr(redis_conf, run_evn):
        return getattr(redis_conf,run_evn)
    else:
        raise my_except.ConfError()

def get_mq_conf():
    '''
    获取mq 配置
    :return:
    '''
    from conf import mq_conf
    if hasattr(mq_conf, run_evn):
        return getattr(mq_conf,run_evn)
    else:
        raise my_except.ConfError()

def get_mongo_conf():
    '''
    获取mongo 配置
    :return:
    '''
    from conf import mongo_conf
    if hasattr(mongo_conf, run_evn):
        return getattr(mongo_conf,run_evn)
    else:
        raise my_except.ConfError()

if __name__ == '__main__':
    pass