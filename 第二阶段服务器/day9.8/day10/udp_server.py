"""
udp套接字服务端程序示例

重点代码 ！！！
"""
from socket import *

# 创建udp套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
udp_socket.bind(('0.0.0.0',8888))

# 接收消息
while True:
    data,addr = udp_socket.recvfrom(1024)
    # 收到exit结束 服务端程序可以一直运行
    # if data == b"exit":
    #     break

    print("From",addr,":",data.decode())
    # 发送消息
    n = udp_socket.sendto(b"Thanks",addr) # 发送字节串
    print("Send %d bytes"%n)

# 关闭套接字
udp_socket.close()

