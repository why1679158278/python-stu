"""
    创建模块module02.py
    在模块中创建全局变量、函数、类(实例方法、类方法)
    在exercise01.py模块中调用
    体会两种导入方式的区别
"""
import module02

# 方式1
# print(module02.data)
# module02.func01()
#
# # 跨模块创建对象 -->  模块名.类名()
# c = module02.MyClass()
# # 调用实例方法
# c.func02()
# # 调用类方法
# module02.MyClass.func03()

# 方式2.1
# from module02 import data
# from module02 import func01
# from module02 import MyClass

# 方式2.2
from module02 import *

print(data)
func01()

c = MyClass()
c.func02()

MyClass.func03()