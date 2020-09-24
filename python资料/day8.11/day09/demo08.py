"""
    面向对象：找人  干嘛
    现实事物  -抽象-> 类  -具体-> 对象
"""


# 先有类还是先有对象?
# 编码：类->对象
# 思想:对象->类

class Wife:
    """
        老婆
    """

    # 数据
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    # 行为(方法=函数)
    def play(self):
        print(self.name, "玩耍")

# 调用构造函数(__init__)
shanger = Wife("双儿", 26, "女")
# 操作对象的数据
shanger.age += 1
print(shanger.age)
# 调用对象的函数
shanger.play()


