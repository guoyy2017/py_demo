#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/2.下午5:11
'''

'''
定时任务模块 apscheduler
'''


from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.schedulers.base import BaseScheduler
from apscheduler.events import EVENT_JOB_EXECUTED,EVENT_JOB_ERROR
import types
import datetime

class TimerWork():

    def __init__(self):
        self.jobs = []
        self.sched = BlockingScheduler()
        self.sched.add_listener(self.listener, EVENT_JOB_ERROR | EVENT_JOB_EXECUTED)

    def listener(self, event):
        if event.exception:
            print 'JOB :<'
        else:
            print 'JOB :>'
        pass

    def exit(self):
        print 'shutdown now'
        self.sched.shutdown(wait=True)
        print 'shutdown ok'
        pass

    def pause(self):
        BaseScheduler.pause_job()
        pass

    def resume(self):
        BaseScheduler.remove_job()
        pass

    def add_job(self, func, gap_time=0, first_run_time=None, args=None, kwargs=None):
        '''
        添加定时任务
        :param func: 执行函数
        :param gap_time: 间隔时间,如果设置小于等于0的值忽略 单位s
        :param first_run_time: 第一次执行时间 datetime.datetime 如果不设置就按正常处理
        :param args: 参数
        :param kwargs: 参数
        :return:
        '''
        self.jobs.append(func)
        if type(first_run_time) == types.IntType:
            first_run_time = datetime.datetime.now() + datetime.timedelta(seconds=first_run_time)
        if gap_time > 0:
            if first_run_time:
                self.sched.add_job(func, 'interval', seconds=gap_time, next_run_time=first_run_time, args=args, kwargs=kwargs)
            else:
                self.sched.add_job(func, 'interval', seconds=gap_time, args=args,
                                   kwargs=kwargs)
        else:
            if first_run_time:
                self.sched.add_job(func, next_run_time=first_run_time, args=args, kwargs=kwargs)
                pass
            else:
                self.sched.add_job(func, args=args, kwargs=kwargs)
                pass
        pass

    def run(self):
        if len(self.jobs) > 0:
            self.sched.start()
        else:
            print 'no add jobs , so check'


if __name__ == '__main__':
    pass