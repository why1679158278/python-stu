"""
event 同步互斥方法
"""

from threading import Thread,Event

msg = None # 线程间消息传递
e = Event() # 事件对象

# 线程函数
def 杨子荣():
    print("杨子荣前来拜山头")
    global msg
    msg = "天王盖地虎"
    e.set() # 结束阻塞

t = Thread(target=杨子荣)
t.start()

# 主线程做验证
print("说对口令就是自己人")
e.wait() # 阻塞等待
if msg == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神,你是对的人")
else:
    print("打死他... 无情啊...")

t.join()




