"""
    迭代器 --> yield
"""


# 需求：for循环操作 自定义对象
class StudentController:
    def __init__(self):
        self.__list_students = []

    def add_student(self, stu):
        self.__list_students.append(stu)

    # def __iter__(self):
    #     index = -1
    #     index += 1
    #     yield self.__list_students[index]
    #
    #     index += 1
    #     yield self.__list_students[index]
    #
    #     index += 1
    #     yield self.__list_students[index]


    def __iter__(self):
        for stu in self.__list_students:
            yield stu

controller = StudentController()
controller.add_student("王其胜")
controller.add_student("符洪民")
controller.add_student("祁帅")

for item in controller:
    print(item)

# 1. 获取迭代器对象
# iterator = controller.__iter__()
# while True:
#     try:
#         # 2. 获取下一个数据
#         item = iterator.__next__()
#         print(item)  #
#     # 3. 如果遇到异常,则停止循环
#     except StopIteration:
#         break
