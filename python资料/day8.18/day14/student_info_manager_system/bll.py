from model import StudentModel


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