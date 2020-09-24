"""
    属性
"""
# 需求：保障数据(年龄)在有效范围内(30-60)
"""
class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age


w01 = Wife("双儿", 9999999999999)
print(w01.name)
print(w01.age)
"""


# 注意：
# 1. 属性名与实例变量名相同
# 2. 属性操作私有变量
class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    @property # age = property(age)
    def age(self):
        return self.__age

    @age.setter # age = age.setter(age)
    def age(self, value):
        if 30 <= value <= 60:
            self.__age = value
        else:
            raise Exception("我不要")


w01 = Wife("双儿", 59)
w01.age = 31
print(w01.name)
print(w01.age)
