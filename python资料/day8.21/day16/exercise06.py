"""
    day16/exercise04 -- 员工列表
    需求：
        定义函数,查找员工列表中薪资大于20000的员工数量
        定义函数,查找员工列表中姓名大于2个字的员工数量
    步骤：
        1. 根据需求，写出函数。
        2. 因为主体逻辑相同,核心算法不同.
           所以使用函数式编程思想(分、隔、做)
           创建通用函数.get_count
        3. 将通用函数添加到IterableHelper类中
        4. 在当前模块中调用
"""
from common.iterable_tools import IterableHelper


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money


# 员工列表
list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]


def get_count_by_money():
    count = 0
    for emp in list_employees:
        if emp.money > 20000:
            count += 1
    return count


def get_count_by_name():
    count = 0
    for emp in list_employees:
        if len(emp.name) > 2:
            count += 1
    return count


print(get_count_by_name())


# 分
def condition01(emp):
    return emp.money > 20000


def condition02(emp):
    return len(emp.name) > 2


def get_count(func):  # 隔
    count = 0
    for emp in list_employees:
        # if len(emp.name) > 2:
        # if condition01(emp):
        # if condition02(emp):
        if func(emp):
            count += 1
    return count


# 做
print(get_count(condition01))

print(IterableHelper.get_count(list_employees, condition01))
