"""
Author: Levi
Email: lvze@tedu.cn
Time : 2020-9-12
Env: Python 3.6
socket and Process exercise
"""
from socket import *

# 服务器地址
HOST = "0.0.0.0"
PORT = 8000
ADDR = (HOST,PORT)

# 处理进入聊天室
def do_login():
    pass

# 框架 启动函数
def main():
    sock = socket(AF_INET,SOCK_DGRAM)
    sock.bind(ADDR)

    # 循环等待接收请求  (总分处理模式)
    while True:
        # 所有请求都在这接收
        data,addr = sock.recvfrom(1024)
        # 将客户端请你去做简单的分割处理
        tmp = data.decode().split(' ')
        # 根据请求选择功能
        if tmp[0] == "L":
            do_login()
        elif tmp[0] == 'C':
            pass

if __name__ == '__main__':
    main()

