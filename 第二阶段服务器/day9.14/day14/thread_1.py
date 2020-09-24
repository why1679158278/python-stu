"""
创建线程基础示例
"""
import threading
from time import sleep
import os

a = 1

# 线程执行函数
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放:葫芦娃")
    global a
    print("a = ",a)
    a = 10000

# 实例化线程对象
t = threading.Thread(target=music)

# 启动线程
t.start()

# 主线程执行内容
for i in range(2):
    sleep(3)
    print(os.getpid(),"播放:中国心")

# 回收线程
t.join()

print("a:",a) # 10000



