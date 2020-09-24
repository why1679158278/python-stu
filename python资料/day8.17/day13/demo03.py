"""
    多态
        语法
"""


class MyClass01:
    def func01(self, a):
        # 1. 调用父
        a.func01()

class MyClassA:
    def func01(self):
        pass

class MyClass02(MyClassA):
    # 2. 子重写
    def func01(self):
        print("222")

m01 = MyClass01()
# 3. 创建子
m01.func01(MyClass02())
