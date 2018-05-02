#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/2.下午2:36
'''

'''
web 管理配置
http://flask-script.readthedocs.io/en/latest/
默认命令可以使用 Server and Shell
runserver
shell
'''

import my_server
from flask_script import Manager,Server

#是否支持跨域
cors = True

app = my_server.create_app()

if cors:
    '''跨域支持'''
    from flask_cors import CORS
    CORS(app=app)

manager = Manager(app=app)

@manager.command
def test():
    print '测试入口'

if __name__ == '__main__':
    #默认执行server 默认端口5000
    manager.add_command('runserver', Server(host='127.0.0.1', port='8000'))
    manager.run(default_command='runserver')
    pass