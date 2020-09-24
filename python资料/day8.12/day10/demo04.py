"""
    私有化
        作用：
            类外无法访问
        做法：
            以双下划线命名   __data
        本质：障眼法
            单下划线+类名+私有变量名字 _MyClass__data
"""


class MyClass:
    def __init__(self, data):
        self.__data = data

    def __func01(self):
        print("func01执行了")


m01 = MyClass(10)
# print(m01.__data)
# print(m01._MyClass__data)

print(m01.__dict__)

# m01.__func01()
# m01._MyClass__func01()
