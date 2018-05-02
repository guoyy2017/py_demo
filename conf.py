#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/2.下午3:56
'''

import os
import my_expect

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
        return mysql_conf[run_evn]
    else:
        raise my_expect.ConfError()

def get_redis_conf():
    '''
    获取redis 配置
    :return:
    '''
    from conf import redis_conf
    if hasattr(redis_conf, run_evn):
        return redis_conf[run_evn]
    else:
        raise my_expect.ConfError()

if __name__ == '__main__':
    pass