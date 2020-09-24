"""
进程池演示

* 进程池中的进程都是子进程,父进程退出进程池随之销毁
"""
from multiprocessing import Pool
from time import sleep,ctime

# 进程池函数
def worker(msg,sec):
    sleep(sec)
    print(ctime(),'---',msg)


# 创建进程池
pool = Pool(4)

# 向进程池中添加事件
for i in range(10):
    msg = "Tedu-%d"%i
    pool.apply_async(worker,args=(msg,2))

# 关闭进程池 不能再添加新事件
pool.close()

# 销毁进程池
pool.join()