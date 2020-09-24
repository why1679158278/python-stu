"""

"""


class Wife:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 30 <= value <= 60:
            self.__age = value
        else:
            # 创建异常  -- 抛出 错误信息
            raise Exception("我不要","if 30 <= value <= 60",1001)

# -- 接收 错误信息
while True:
    try:
        age = int(input("请输入你老婆年龄："))
        w01 = Wife(age)
        break
    except Exception as e:
        print(e.args)
