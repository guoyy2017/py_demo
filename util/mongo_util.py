#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/3.下午5:48
'''

'''
mongo 工具包
'''

import my_conf
from pymongo import MongoClient

db_info = my_conf.get_mongo_conf()

def get_client():
    '''
    获取一个连接
    :return:
    '''
    client = MongoClient(db_info['db_host'], db_info['db_port'])
    return client

def get_db(db_name=None):
    '''
    获取一个db 操作
    :param db_name:
    :return:
    '''
    name = db_name
    if  name == None:
        name = db_info['db_name'] #获取默认db
    client = get_client()
    return client[name]

if __name__ == '__main__':
    pass