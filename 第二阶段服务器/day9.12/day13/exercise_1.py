"""
100000以内质数之和
"""

import time
from multiprocessing import Process

# 装饰器函数求一个函数的运行时间
def timeis(f):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = f(*args,**kwargs)
        end_time = time.time()
        print("执行时间:",end_time-start_time)
        return res
    return  wrapper

# 判断一个数是否为质数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n//2 + 1):
        if n % i == 0:
            return False
    return True

# @timeis
# def no_process():
#     prime = [] # 存放100000以内的质数
#     for i in range(100001):
#         if isPrime(i):
#             prime.append(i)
#     print(sum(prime)) # 求和

class Prime(Process):
    def __init__(self,begin,end):
        self.begin = begin # 起始数字
        self.end = end # 结尾数字
        super().__init__()

    # 求和
    def run(self):
        prime = []
        for i in range(self.begin,self.end):
            if isPrime(i):
                prime.append(i)
        print(sum(prime))

@timeis
def multi_process(n):
    # n 表示你想创建几个进程 25000  10000
    tep = 100000 // n
    jobs = []
    # 循环创建进程
    for i in range(1,100001,tep):
        p = Prime(i,i+tep)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs] # 回收进程

# no_process() # 执行时间: 15.282682657241821

# multi_process(4) # 执行时间: 8.93787693977356

# multi_process(10) # 执行时间: 8.05749797821045

