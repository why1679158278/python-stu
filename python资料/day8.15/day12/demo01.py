"""
    继承
        皇位：江山不用太子打,但是可以直接坐.
        财产：钱不用孩子挣,但是可以直接花.
        编程：代码不用子类写,但是可以直接用.
"""

"""
class Student:
    def say(self):
        print("说话")

    def play(self):
        print("玩耍")


class Teacher:
    def say(self):
        print("说话")

    def teach(self):
        print("教学")
"""


# 设计角度：先有子类再有父类
# 编码角度：先有父类再有子类
class Person:
    def say(self):
        print("说话")


class Teacher(Person):
    def teach(self):
        self.say()
        print("教学")


class Student(Person):
    def play(self):
        self.say()
        print("玩耍")


qtx = Teacher()
qtx.teach()
p = Person()

# 内置函数 - 用于判断关系的函数
# 是一种的关系
# 对象 是一种 类型： isinstance(对象,类型)
# 老师对象 是一种 老师类型
print(isinstance(qtx, Teacher))  # True
# 老师对象 是一种 人类型
print(isinstance(qtx, Person))  # True
# 老师对象 是一种 学生类型
print(isinstance(qtx, Student))  # False
# 人对象 是一种 学生类型
print(isinstance(p, Student))  # False

# 类型 是一种 类型： issubclass(类型,类型)
# 老师类型 是一种 老师类型
print(issubclass(Teacher, Teacher))  # True
# 老师类型 是一种 人类型
print(issubclass(Teacher, Person))  # True
# 老师类型 是一种 学生类型
print(issubclass(Teacher, Student))  # False
# 人类型 是一种 学生类型
print(issubclass(Person, Student))  # False

# 是的关系
# 老师对象的类型 是 老师类型
print(type(qtx) == Teacher)  # True
# 老师对象的类型 是 人类型
print(type(qtx) == Person)  # False
