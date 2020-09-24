"""
创建套接字示例
"""
import socket

# 创建套接字对象 UDP服务
upd_socket = socket.socket(socket.AF_INET,
                           socket.SOCK_DGRAM)

# 绑定地址
upd_socket.bind(('127.0.0.1',8888)) # 测试地址
upd_socket.bind(('172.40.91.202',8888)) # 网络IP地址
upd_socket.bind(('0.0.0.0',8888)) # 自动匹配地址