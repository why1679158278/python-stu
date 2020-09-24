from bll import StudentController
from model import StudentModel


class StudentView:
    """
        学生界面视图
            负责处理界面逻辑(输入/输出)
    """

    def __init__(self):
        self.__controller = StudentController()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("1. 添加学生信息")
        print("2. 显示学生信息")
        print("3. 删除学生信息")
        print("4. 修改学生信息")

    def __select_menu(self):
        item = input("请输入您的选项：")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__display_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__change_student()

    def __input_student(self):
        stu = StudentModel()
        stu.name = input("请输入学生姓名：")
        stu.sex = input("请输入学生性别：")
        stu.score = int(input("请输入学生成绩："))
        stu.age = int(input("请输入学生年龄："))
        self.__controller.add_student(stu)

    def __display_students(self):
        for stu in self.__controller.list_students:
            print(stu)
            # print(f"{stu.name}的编号是{stu.sid},年龄是{stu.age},性别是{stu.sex},成绩是{stu.score}")

    def __delete_student(self):
        sid = int(input("请输入需要删除的学生编号："))
        if self.__controller.remove_student(sid):
            print("删除成功")
        else:
            print("删除失败")

    def __change_student(self):
        stu = StudentModel()
        stu.sid = int(input("请输入需要修改的学生编号："))
        stu.name = input("请输入需要修改的学生姓名：")
        stu.sex = input("请输入需要修改的学生性别：")
        stu.score = int(input("请输入需要修改的学生成绩："))
        stu.age = int(input("请输入需要修改的学生年龄："))
        if self.__controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")