"""
 网络客服对话

你在客户端可以输入你的问题，服务端会给你回发问题
，客户端接收到回发之后打印即可

要求 ： 可以同时多个客户端一起问问题
"""

from socket import *

# 小美问答字典
request = {'几岁':'我2岁了',
           '男生女生':"我是机器人",
           '你好':"你好啊"
           }

# 创建tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)
# 绑定地址
tcp_socket.bind(('0.0.0.0',8888))
# 设置监听
tcp_socket.listen(5)

while True:
    # 处理客户端链接 (阻塞函数)
    connfd,addr = tcp_socket.accept()
    # 接收问题
    data = connfd.recv(1024).decode()
    # 循环遍历字典
    for key in request:
        # 找到对应问题
        if key in data:
            connfd.send(request[key].encode())
            break
    else:
        connfd.send("人家还小，不太懂".encode())

    connfd.close()

# 关闭套接字
tcp_socket.close()