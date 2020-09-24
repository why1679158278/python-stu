"""
     员工管理器2.0
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
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def get_salary(self):
        return self.base_salary


class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        super().__init__(base_salary)
        self.bonus = bonus

    def get_salary(self):
        return super().get_salary() + self.bonus


class Tester(Employee):
    def __init__(self, base_salary, bug_count):
        super().__init__(base_salary)
        self.bug_count = bug_count

    def get_salary(self):
        return super().get_salary() + self.bug_count * 5


# ---------------------
manager = EmployeeManager()
manager.add_employee(Programmer(8000, 1000000))
manager.add_employee(Tester(5000, 500))

print(manager.calculate_total_salary())
