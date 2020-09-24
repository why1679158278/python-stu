"""
    以面向对象思想,描述下列情景.
    小明请保洁打扫卫生
        1. 识别对象
                人类       保洁类
        2. 分配职责
                请(通知)   打扫卫生
        3. 建立交互
            (1)
            (2)
            (3)
"""

# 写法1：每次通知新保洁
"""
class Client:
    def __init__(self, name=""):
        self.name = name

    def notify(self):
        cleaner = Cleaner()
        cleaner.cleaning()

class Cleaner:
    def cleaning(self):
        print("打扫卫生")


xm = Client("小明")
xz = Client("小赵")
xm.notify()
"""
# 写法2: 小明通知自己的保洁
"""
class Client:
    def __init__(self, name=""):
        self.name = name
        self.cleaner = Cleaner()

    def notify(self):
        self.cleaner.cleaning()

class Cleaner:
    def cleaning(self):
        print("打扫卫生")


xm = Client("小明")
xm.notify()
"""
# 写法3：小明不创建保洁,而是通过参数传递。
class Client:
    def __init__(self, name=""):
        self.name = name

    # def notify(self,cleaner):
    #     cleaner.cleaning()

    def notify(self,cleaner):
        cleaner.cleaning()

class Cleaner:
    def cleaning(self):
        print("打扫卫生")

xm = Client("小明")
c01 = Cleaner()
xm.notify(c01)