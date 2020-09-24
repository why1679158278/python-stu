"""
    module02模块
    在exercise01.py模块中调用
    体会两种导入方式的区别
"""
data = 100


def func01():
    print("func01执行喽")


class MyClass:
    def func02(self):
        print("func02执行喽")

    @classmethod
    def func03(cls):
        print("func03执行喽")
