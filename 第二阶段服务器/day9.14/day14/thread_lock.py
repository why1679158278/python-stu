"""
线程锁
"""
from threading import Thread,Lock

a = b = 0
lock = Lock() # 锁对象

def value():
    while True:
        lock.acquire()
        if a != b:
            print("a = %d,b = %d"%(a,b))
        lock.release()

t = Thread(target = value)
t.start()

while True:
    with lock:  # 上锁
        a += 1
        b += 1
    # with结束自动解锁


t.join()
