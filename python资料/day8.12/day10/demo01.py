"""
    实例成员
        字面意思：对象(具体)的 变量 与 方法
        实例变量:自己的数据
            价值：每个对象都有一份
            创建：
                 对象.变量名 = 数据
            使用：
                　对象.变量名
        实例方法:操作实例变量
            创建：
                def 方法名(self,参数)
                    方法体
            使用：
                对象.方法名(参数)

"""


class Wife:
    def __init__(self, name):
        self.name = name

    def print_self(self):
        print("我是：", self.name)


w01 = Wife("丽丽")  # dict01 = {"name":"丽丽"}
w01.name = "莉莉"  # dict01["name"] = "莉莉"
print(w01.name)  # print(dict01["name"])

w01.print_self()

print(w01.__dict__)  # {"name":"丽丽"}

"""
# 支持动态创建类成员
# 类中的成员应该由类的创造者决定
class Wife:
    pass

w01 = Wife()
w01.name = "莉莉"
print(w01.name)#对象.变量名
"""

"""
# 实例变量的创建要在构造函数中__init__
class Wife:
    def set_name(self,name):
        self.name = name


w01 = Wife()
w01.set_name("丽丽")
print(w01.name)
"""
