#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/3.上午11:56
'''

'''
爬取任务 多种模式
'''

import time

def test(name):
    print 'nihao %s' % name

def multi_process():
    '''
    多进程模式
    multiprocessing Process Pool
    multiprocessing.current_process().name   #获取当前线程的名字
    Process
    p = Process(target=func, args=(*,*))
    p.start()
    p.join()

    Pool apply_async 不会阻塞 apply 主进程会阻塞
    res = apply_async()
    res.get() #获取异步执行结果
    reses = Pool.map(func,params) #阻塞执行
    :return:
    '''
    from multiprocessing import Pool
    pool = Pool(processes=2)
    for i in range(10):
        pool.apply_async(test, (str(i),)) #异步开启进程, 非阻塞型
    time.sleep(10)
    pool.close() # 关闭pool, 则不会有新的进程添加进去
    pool.join() # 必须在join之前close, 然后join等待pool中所有的线程执行完毕
    pass

def multi_thread():
    '''
    多线程模式 thread
    :return:
    '''
    pass

def multi_coroutine():
    '''
    非cpu密集型可用
    多协程 gevent
    :return:
    '''
    from gevent import monkey
    import gevent
    from gevent.pool import Group
    monkey.patch_socket()
    #以上都是准备工作
    g = Group()
    for i in range(10):
        g.add(gevent.spawn(test, (str(i),)))
    g.join()
    pass

def multi_timer():
    '''
    多任务 定时器处理
    apscheduler
    :return:
    '''
    pass

if __name__ == '__main__':
    pass