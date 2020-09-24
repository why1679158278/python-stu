"""
udp 客户端
重点代码 ！！！
"""
from socket import *

# 服务器地址
ADDR = ("127.0.0.1",8888)

# 创建udp套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 发送后接收，与服务端配合
while True:
    msg = input(">>")
    # 直接回车退出，不用管服务器
    if not msg:
        break
    udp_socket.sendto(msg.encode(),ADDR) # 发送字节串
    # 输入exit结束循环
    # if msg == 'exit':
    #     break
    data,addr = udp_socket.recvfrom(1024)
    print("From server:",data.decode())

# 关闭套接字
udp_socket.close()