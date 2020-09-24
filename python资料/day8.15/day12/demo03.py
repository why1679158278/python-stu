"""
    内置可重写函数
        __str__
"""


class Person(object):
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    # 重写：彰显子类的个性(与别人不同)
    # 对象 --> 字符串:给人看的(没有语法限制)
    def __str__(self):
        return f"{self.name}的年龄是{self.age}"

wk = Person("悟空", 26)
# <__main__.Person object at 0x7fbabfbc3e48>
print(wk)
# message = wk.__str__()
# print(message)
