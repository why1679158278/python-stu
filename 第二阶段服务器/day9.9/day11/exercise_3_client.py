from socket import *

while True:
    msg = input("我：")
    if not msg:
        break

    # 创建套接字，完成一次消息的收发后就关闭
    tcp_socket = socket()
    tcp_socket.connect(('127.0.0.1',8888))
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print("小美：",data.decode())
    tcp_socket.close()