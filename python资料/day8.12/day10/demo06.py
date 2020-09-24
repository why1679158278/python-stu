"""
    属性原理
        目标：保护实例变量
        理念：拦截对变量的操作，改为对方法的调用.
        一个属性对象,包装了两个方法(负责读取 负责写入).
"""

class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
        # self.set_age(age)


    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 30 <= value <= 60:
            self.__age = value
        else:
            raise Exception("我不要")

    # @property 原理如下
    age = property(get_age)
    # age.setter 原理如下
    age = age.setter(set_age)


w01 = Wife("双儿", 59)
w01.age = 300
print(w01.name)
print(w01.age)
