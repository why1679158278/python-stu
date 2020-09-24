"""
    迭代器
"""


class StudentIterator:
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        if self.__index == len(self.__data) - 1:
            raise StopIteration()
        self.__index += 1
        return self.__data[self.__index]


# 需求：for循环操作 自定义对象
class StudentController:
    def __init__(self):
        self.__list_students = []

    def add_student(self, stu):
        self.__list_students.append(stu)

    def __iter__(self):
        return StudentIterator(self.__list_students)


controller = StudentController()
controller.add_student("王其胜")
controller.add_student("符洪民")
controller.add_student("祁帅")

# for item in controller:
#     print(item)

# 1. 获取迭代器对象
iterator = controller.__iter__()
while True:
    try:
        # 2. 获取下一个数据
        item = iterator.__next__()
        print(item)  #
    # 3. 如果遇到异常,则停止循环
    except StopIteration:
        break
