"""
    学生信息管理系统
        View 打印学生信息时,重写了__str__
        Controller 删除学生时,重写了__eq__

    练习：修改employee_info_manager_system.py
"""

class StudentModel:
    """
        学生模型
            用于封装V与C传递的数据
    """

    def __init__(self, name="", sex="", score=0.0, age=0, sid=0):
        self.name = name
        self.sex = sex
        self.score = score
        self.age = age
        self.sid = sid

    def __str__(self):
        return f"{self.name}的编号是{self.sid},年龄是{self.age},性别是{self.sex},成绩是{self.score}"

    def __eq__(self, other):
        return self.sid == other.sid


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


class StudentController:
    """
        学生控制器
            对学生信息的核心处理逻辑(添加/删除/修改..)
    """

    def __init__(self):
        self.__list_students = []
        self.__start_id = 1000

    @property
    def list_students(self):
        return self.__list_students

    def add_student(self, stu_target):
        """
            添加学生信息
        :param stu_target:目标学生
        """
        stu_target.sid = self.__start_id
        self.__start_id += 1

        self.__list_students.append(stu_target)

    def remove_student(self, sid):
        """
            移除学生
        :param sid:学生编号
        :return: 是否移除成功
        """
        stu = StudentModel(sid=sid)
        if stu in self.__list_students:
            # 需要重写StudentModel的__eq__方法
            self.__list_students.remove(stu)
            return True
        return False

        # for i in range(len(self.__list_students)):
        #     if self.__list_students[i].sid == sid:
        #         del self.__list_students[i]
        #         return True  # 删除成功
        # return False  # 删除失败

    def update_student(self, stu_target):
        for stu in self.__list_students:
            if stu.sid == stu_target.sid:
                stu.sex = stu_target.sex
                stu.name = stu_target.name
                stu.age = stu_target.age
                stu.score = stu_target.score
                return True
        return False


# 入口
view = StudentView()
view.main()
