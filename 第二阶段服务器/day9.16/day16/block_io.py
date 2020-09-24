"""
非阻塞IO示例
"""

from socket import *
import time

log = open("my.log",'a') # 日志文件

# 创建tcp套接字
sockfd = socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(5)

# 设置非阻塞
# sockfd.setblocking(False)

# 设置超时时间 3s
sockfd.settimeout(3)

while True:
    try:
        print("Waiting for connect")
        connfd,addr = sockfd.accept()
        print("Connect from",addr)
    except BlockingIOError as e:
        # 做一些和 accept 无关的IO事情
        msg = "%s : %s\n"%(time.ctime(),e)
        log.write(msg)
        log.flush()
        time.sleep(2)
    except timeout as e:
        msg = "%s : %s\n" % (time.ctime(), e)
        log.write(msg)
        log.flush()
    else:
        # 有客户端链接
        data = connfd.recv(1024)
        print(data.decode())