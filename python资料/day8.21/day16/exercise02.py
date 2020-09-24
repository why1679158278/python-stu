# 练习1：使用Student封装以下三个列表中数据
#       创建学生列表
#       创建学生类 --> 根据列表创建学生对象
list_student_name = ["赵晗旭", "朱林", "钱涛"]
list_student_age = [28, 25, 26]
list_student_sex = ["女", "男", "男"]


class Student:
    def __init__(self, name="", age=0, sex=""):
        self.name = name
        self.age = age
        self.sex = sex


# for item in zip(list_student_name, list_student_age, list_student_sex):
#     print(item)

# 写法1:
# list_students = []
# for item in zip(list_student_name, list_student_age, list_student_sex):
#     stu = Student(item[0],item[1],item[2])
#     list_students.append(stu)
# print(list_students)


# list_students = []
# for item in zip(list_student_name, list_student_age, list_student_sex):
#     stu = Student(*item)  # 一个元组 拆 多个元素
#     list_students.append(stu)
# print(list_students)

# 写法2:
list_student_infos = [
    ["赵晗旭", "朱林", "钱涛"],
    [28, 25, 26],
    # ["女", "男", "男"]
]

list_students = []
for item in zip(*list_student_infos):
    stu = Student(*item)  # 一个元组 拆 多个元素
    list_students.append(stu)
print(list_students)
