class EmployeeModel(object):
    def __init__(self, eid=0, did=0, name="", money=0.0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

    def __str__(self):
        return f"{self.name}的员工编号是{self.eid}"

    def __eq__(self, other):
        return self.eid == other.eid


class EmployeeView:
    """
        员工界面视图
            负责处理界面逻辑(输入/输出)
    """

    def __init__(self):
        self.__controller = EmployeeController()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("1. 添加员工信息")
        print("2. 显示员工信息")
        print("3. 删除员工信息")
        print("4. 修改员工信息")

    def __select_menu(self):
        item = input("请输入您的选项：")
        if item == "1":
            # 先写方法调用语句,再alt + 回车,自动生成创建方法代码.
            self.__input_employee()
        elif item == "2":
            self.__display_employees()
        elif item == "3":
            self.__delete_employee()
        elif item == "4":
            self.__change_employee()

    def __input_employee(self):
        emp = EmployeeModel()
        emp.did = int(input("请输入部门编号："))
        emp.name = input("请输入员工姓名：")
        emp.money = int(input("请输入员工薪资："))
        emp.age = int(input("请输入员工年龄："))
        self.__controller.add_employee(emp)

    def __display_employees(self):
        for emp in self.__controller.list_employees:
            print(emp)

    def __delete_employee(self):
        sid = int(input("请输入需要删除的员工编号："))
        if self.__controller.remove_employee(sid):
            print("删除成功")
        else:
            print("删除失败")

    def __change_employee(self):
        emp = EmployeeModel()
        emp.eid = int(input("请输入需要修改的员工编号："))
        emp.did = int(input("请输入需要修改的部门编号："))
        emp.name = input("请输入需要修改的员工姓名：")
        emp.money = input("请输入需要修改的员工工资：")
        if self.__controller.update_employee(emp):
            print("修改成功")
        else:
            print("修改失败")


class EmployeeController:
    """
        员工控制器
            对员工信息的核心处理逻辑(添加/删除/修改..)
    """

    def __init__(self):
        self.__list_employees = []
        self.__start_id = 1000

    @property
    def list_employees(self):
        return self.__list_employees

    def add_employee(self, emp_target):
        """
            添加员工信息
        :param stu_target:目标员工
        """
        emp_target.eid = self.__start_id
        self.__start_id += 1

        self.__list_employees.append(emp_target)

    def remove_employee(self, eid):
        """
            移除员工
        :param sid:员工编号
        :return: 是否移除成功
        """

        emp = EmployeeModel(eid)
        if emp in self.__list_employees:
            self.__list_employees.remove(emp)
            return True
        return False

    def update_employee(self, emp_target):
        for emp in self.__list_employees:
            if emp.eid == emp_target.eid:
                emp.money = emp_target.money
                emp.name = emp_target.name
                emp.did = emp_target.did
                return True
        return False


# 入口
view = EmployeeView()
view.main()
