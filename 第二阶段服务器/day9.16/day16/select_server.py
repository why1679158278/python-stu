"""
基于 select 方法的IO多路复用并发模型

重点代码 !!
"""
from socket import *
from select import select

# 创建监听套接字,作为初始监控对象
sockfd = socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(5)

# 设置为非阻塞
sockfd.setblocking(False)

# 设置关注列表
rlist = [sockfd] # 关注监听套接字
wlist = []
xlist = []

# 循环监控关注的IO
while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    # 遍历就绪的IO列表,分情况讨论 监听套接字和客户端连接套接字
    for r in rs:
        if r is sockfd:
            connfd, addr = r.accept()
            print("Connect from",addr)
            # 将链接进来的客户端链接套接字加入关注的IO
            connfd.setblocking(False)
            rlist.append(connfd)
        else:
            # 某个客户端发送了消息
            data = r.recv(1024).decode()
            if not data:
                # 客户端结束
                rlist.remove(r) # 取消关注
                r.close()
                continue # for循环继续遍历后面的IO
            print(data)
            # r.send(b'OK')
            wlist.append(r) # 加入到写关注列表

    for w in ws:
        w.send(b'ok')
        wlist.remove(w) # 移除
