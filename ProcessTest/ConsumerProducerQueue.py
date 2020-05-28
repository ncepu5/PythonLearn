import time
import random
from multiprocessing import Process,Queue

def producer(q,name,food):
    for i in range(2):
        time.sleep(random.random())
        fd = '%s%s'%(food,i)
        q.put(fd)
        print('%s生产了一个%s'%(name,food))

def consumer(q,name):
    while True:
        food = q.get()
        if not food:break
        time.sleep(random.randint(1,3))
        print('%s吃了%s'%(name,food))


def cp(c_count,p_count):
    q = Queue(10)
    for i in range(c_count):
        Process(target=consumer, args=(q, '灰太狼')).start()
    p_l = []
    for i in range(p_count):
        p1 = Process(target=producer, args=(q, '喜洋洋', '包子'))
        p1.start()
        p_l.append(p1)
    for p in p_l:p.join()
    for i in range(c_count):
        q.put(None)

if __name__ == '__main__':
    cp(2,3)