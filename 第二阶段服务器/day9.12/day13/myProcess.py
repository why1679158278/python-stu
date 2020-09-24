"""
自定义进程类
"""

from multiprocessing import Process

# 如果进程执行的时间比较复杂,封装在一个类里
class MyProcess(Process):
    def __init__(self,value):
        self.value = value
        # 同时加载父类属性
        super().__init__()

    def fun(self):
        print("假装干了个大事")

    # start()时run会作为一个新的进程内容执行
    def run(self):
        self.fun()
        print("完事了")

p = MyProcess(2)
p.start() # 启动进程 -->run就会运行
p.join()



# class Process:
#     def __init__(self,target):
#         self.target = target
#
#     def run(self):
#         self.target()
#
#     def start(self):
#         self.run()