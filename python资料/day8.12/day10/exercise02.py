"""
    对象计数器
        统计构造函数执行的次数
        使用类变量实现
"""


class Wife:
    count = 0

    @classmethod
    def print_count(cls):
        print("娶了%d个" % cls.count)

    def __init__(self, name=""):
        self.name = name
        Wife.count += 1

w01 = Wife("双儿")
w02 = Wife("阿珂")
w03 = Wife("苏荃")
w04 = Wife("丽丽")
w05 = Wife("芳芳")

print(w05.count)

Wife.print_count()# print_count(Wife)