"""
    一家公司，有如下几种岗位
        程序猿：底薪 + 项目分红
        测试员：底薪 + Bug数量 * 5
        .....

    创建员工管理器
        1. 计算所有员工
        2. 计算总薪资

    三大特征：
        封装：分
            创建员工管理器、程序猿、测试员类
        继承：隔
            创建员工类
        多态：做
            在程序猿、测试员类中通过重写定义薪资算法

    六大原则：
        开闭原则：
            增加新岗位,不影响员工管理器.
        单一职责：
            员工管理器：统一管理所有员工
            程序员：底薪+分红
            测试员：底薪+bug数×5
        依赖倒置：
            员工管理器用员工类,不用程序员/测试员
        组合复用：
            员工管理器通过实例变量调用员工薪资算法
"""


class EmployeeManager:
    def __init__(self):
        self.__list_employees = []

    def add_employee(self, emp):
        self.__list_employees.append(emp)

    def calculate_total_salary(self):
        total_salary = 0
        for emp in self.__list_employees:
            # 调用父执行子
            total_salary += emp.get_salary()
        return total_salary


class Employee:
    def get_salary(self):
        pass


class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        self.base_salary = base_salary
        self.bonus = bonus

    def get_salary(self):
        return self.base_salary + self.bonus


class Tester(Employee):
    def __init__(self, base_salary, bug_count):
        self.base_salary = base_salary
        self.bug_count = bug_count

    def get_salary(self):
        return self.base_salary + self.bug_count * 5


# ---------------------
manager = EmployeeManager()
manager.add_employee(Programmer(8000, 1000000))
manager.add_employee(Tester(5000, 500))

print(manager.calculate_total_salary())
