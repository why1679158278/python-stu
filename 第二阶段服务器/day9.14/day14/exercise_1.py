"""
练习1:  模拟一个售票系统
有 500 张门票 记为 T1---T500 存入到一个列表里

创建 10 个线程 同时进行售票 ,知道所有的票都卖完

票需要按照顺序卖出

每出一张打印 w1 --- T256 每出一张票需要sleep(0.1)

"""
from threading import Thread
from time import sleep

# 模拟500张票
ticket = ["T%d"%x for x in range(1,501)]

# 线程函数 w 相当于窗口名
def sell(w):
    while ticket:
        sleep(0.1)
        print("%s -- %s"%(w,ticket.pop(0)))


# 创建线程
jobs = []
for i in range(1,11):
    t = Thread(target=sell,args=("W%d"%i,))
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()






