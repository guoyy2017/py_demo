#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/2.下午2:36
'''

'''
后台任务模块
执行方法 python task.py method args1 args2 --kwargs1 val1 --kwargs2 val2
执行task 方法如下 python task.py timer_task --task demo_task --method test
__import__ 用法中 fromlist 参数的重要性 fromlist=True 可以引入包内模块，否则只能引用包
func.__code__.co_varnames 获取参数列表
func.__code__.co_argcount 获取参数总数
func.__defaults__ 获取默认值列表
默认值后不能有没有默认值的参数存在
'''

import fire
import logging
import traceback
import types
# try:
#     from task import *
# except:
#     pass

class DEAL(object):

    def test(self, *args, **kwargs):
        print args
        print kwargs
        pass

    def timer_task(self, *args, **kwargs):
        '''
        配置定时任务启动
        :param args:
        :param kwargs: {'task':'任务模块','method':'任务方法,默认run'*} *可以缺省
        :return:
        '''
        if 'task' in kwargs:
            try:
                task = kwargs['task']
                method = 'run'
                if 'method' in kwargs:
                    method = kwargs['method']
                logging.info('deal %s %s ' % (task, method))
                obj = __import__('task.%s' % task, fromlist=True)
                func = getattr(obj, method, None)
                if type(func) == types.NoneType:
                    logging.error('no find func %s %s ' % (task, method))
                else:
                    func()
                # eval('%s.%s()' % (task, method))
            except:
                traceback.print_exc()
                pass
        else:
            logging.error('loss task params,check please')
        pass

if __name__ == '__main__':
    fire.Fire(DEAL)
    pass