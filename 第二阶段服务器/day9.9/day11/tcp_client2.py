"""
tcp客户端示例2
多个客户端循环发送消息

重点代码！！
"""
from socket import *

# 循环发送消息
# 每次发送消息都需要重新建立套接字，发起链接，效率较低
while True:
    msg = input(">>")
    if not msg:
        break

    # 创建套接字，完成一次消息的收发后就关闭
    tcp_socket = socket()
    tcp_socket.connect(('127.0.0.1',8888))
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print("from Server：",data.decode())
    tcp_socket.close()