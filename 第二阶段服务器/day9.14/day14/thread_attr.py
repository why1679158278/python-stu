"""
线程属性说明
"""

from threading import Thread
from time import  sleep

def fun():
    sleep(3)
    print("线程属性测试")

t = Thread(target= fun)

# 设置分支线程随主线程退出
t.setDaemon(True)

t.start()

t.setName("tarena")
print("Name:",t.getName())

print("is alive:",t.is_alive())




