# 1、使用多线程请求一定数量的 httpbin 网站页面并存储结果，地址格式 http://httpbin.org/get?a=X（X为不同的数字），线程数为5，控制并发数量为3，使用线程池或者信号量都可以；使用队列1提交全部任务10个，使用队列2存储不同线程执行的结果。为了让结果随机，可以随机sleep一点点时间。
from time import sleep
from queue import Queue
from threading import Thread, Semaphore, current_thread


def get():
    tasks_queue = Queue()
    results_queue = Queue()
    sema = Semaphore(3) #信号量
    threads = []
    results = dict(list)
    URL = 'http://httpbin.org/get?a={}'


    def foo():
        while 1:
            with sema:
                if tasks_queue.empty():
                    break
                value = tasks_queue.get()
                result =get(URL.format(value))
                results_queue.put((result))
                sleep(0.1)


    for i in range(10):
        tasks_queue.put(i)

    for i in range(5):
        t = Thread(target=foo, name=f'{i}')
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    while 1:
        if results_queue.empty():
            break
        result = results_queue.get()
        print(f'result:{result}')



# 2、使用多进程实现生产者/消费者模型，而且可以通过生产者控制消费者是否接收新的任务。启动2个消费者；前5个任务由其中一个消费者接收执行，剩下的由另外的消费者单独接收执行
from time import sleep
from random import random, randint
from multiprocessing import Process, JoinableQueue, current_process, Event#Event（事件）：事件处理的机制：全局定义了一个内置标志Flag，如果Flag值为 False，那么当程序执行 event.wait方法时就会阻塞，如果Flag值为True，那么event.wait 方法时便不再阻塞。

def get():
    TIMEOUT = 2
    tasks_queue = JoinableQueue()
    event1 = threading.Event()
    event2 = threading.Event()
    map = {
        0: event1,
        1: event2
    }




    def producer():
        t = threading.currentThread()
        for i in range(10):
            integer = randint(1, 100)
            tasks_queue.put(integer)
            if i <= 5:
                event1.set()
            else:
                event1.clear()
                event2.set()
            print(f'Producer: {integer}')
            sleep(0.1)
        event1.set()

    def consumer(event):
        t=threading.currentThread()
        while 1:
            event_is_set = event.wait(TIMEOUT)
            if event_is_set:
                integer = tasks_queue.pop()
                if integer is None:
                    break
                print(f'{current_process().name}: {integer}')
                tasks_queue.task_done()

    processes = []
    p = Process(target=producer)
    p.start()
    processes.append(p)
    for i in range(2):
        p = Process(target=consumer, name=f'Consumer{i}', args=(map.get(i),))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()



# 3、使用多进程模块写一个使用优先级队列的例子
import time
import threading
from random import randint
from queue import PriorityQueue
import multiprocessing



def worker():
    print(2+3)


if __name__=='__main__':
    que = PriorityQueue()
    que.put(10)
    que.put(1)
    que.put(5)
    while not que.empty():
        print(que.get())
    p=multiprocessing.Process(target=worker,)
    p.start()




