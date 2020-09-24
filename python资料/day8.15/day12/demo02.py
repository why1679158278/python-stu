class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

"""
# 子类没有构造函数,会使用继承而来的父类构造函数.
class Student(Person):
    pass

s01 = Student("悟空",26)
print(s01.name)
print(s01.age)
"""

# 子类有构造函数,不会使用继承而来的父类构造函数.
# 【子覆盖了父方法,好像它不存在】
class Student(Person):
    # 子类构造函数：父类构造函数参数,子类构造函数参数
    def __init__(self, name, age, score):
        # 调用父类构造函数
        super().__init__(name, age)

        self.score = score

ls = Person("李四",22)
s02 = Student("张三", 23, 100)
print(s02.name)
