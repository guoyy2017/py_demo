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
    多线程模式 thread threadpool
    :return:
    '''
    import threadpool
    pool = threadpool.ThreadPool(num_workers=2) #工作线程数
    params = []
    for i in range(10):
        params.append(i)
    requests = threadpool.makeRequests(test, params)
    [pool.putRequest(req) for req in requests] #具体执行
    pool.wait() #等待结束
    pool.dismissWorkers(num_workers=2)  #销毁池
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

def multi_concurrent():
    '''
    多线程 多进程用法 计算密集型使用多进程，多线程效果不佳，还会变慢
    from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Executor
    multiprocessing开销比较大，原因就在于：主进程和子进程之间通信，必须进行序列化和反序列化的操作
    https://www.cnblogs.com/kangoroo/p/7628092.html
    '''
    from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Executor
    #多线程
    pool = ThreadPoolExecutor(max_workers=2) #最大工作线程数
    res = pool.map(test, (1,2,3)) #执行
    #多进程
    pool = ProcessPoolExecutor(max_workers=2) #最大工作进程数
    res = pool.map(test, (1, 2, 3))  # 执行

    pass

if __name__ == '__main__':
    pass