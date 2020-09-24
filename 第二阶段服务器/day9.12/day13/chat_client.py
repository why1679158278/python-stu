"""
聊天室客户端
"""
from socket import *
from multiprocessing import Process

# 服务器地址
ADDR = ('127.0.0.1',8000)

def login(sock):
    while True:
        name = input("请输入姓名:")
        # 发送请求
        msg = "L "+name
        sock.sendto(msg.encode(),ADDR)
        # 等待回复
        data,addr = sock.recvfrom(1024)
        # 根据情况处理
        if data.decode() == 'OK':
            print("您已进入聊天室")
            return
        else:
            print("该用户已存在")


def main():
    sock = socket(AF_INET,SOCK_DGRAM)

    # 进入聊天室
    login(sock)


if __name__ == '__main__':
    main()