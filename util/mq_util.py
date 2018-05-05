#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/3.下午5:48
'''

'''
mq 工具包
'''

import pika
import my_conf

db_info = my_conf.get_mq_conf()

def get_conn():
    '''
    获取连接
    :return:
    '''
    credentials = pika.PlainCredentials(db_info['db_user'], db_info['db_passwd'])
    conn = pika.BlockingConnection(pika.ConnectionParameters(host=db_info['db_host'],
                                                             port=db_info['db_port'],
                                                             virtual_host=db_info['db_virtual_host'],
                                                             credentials=credentials))
    return conn

def close_conn(conn):
    '''
    关闭连接
    :param conn:
    :return:
    '''
    try:
        conn.close()
    except:
        pass

if __name__ == '__main__':
    pass