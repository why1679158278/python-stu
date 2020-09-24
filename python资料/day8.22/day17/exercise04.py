"""
    需求：
        定义函数,获取所有员工的姓名
        定义函数,获取所有员工的员工编号与薪资
    步骤：
    1. 根据需求，写出函数。
    2. 创建通用函数.
        分： 脑补变化点函数
            创建通用函数
        隔：使用参数抽象变化点函数
        做：在调用通用函数时,传递lambda.
    3. 将通用函数添加到IterableHelper类中 select
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

"""
def select_name(list_target):
    for emp in list_target:
        yield emp.name


def select_eid_and_money(list_target):
    for emp in list_target:
        yield (emp.name, emp.money)


for item in select_name(list_employees):
    print(item)


# def handle01(emp):
#     return emp.name
#
# def handle02(emp):
#     return (emp.name, emp.money)

def select(list_target, func):
    for emp in list_target:
        # yield handle01(emp)
        # yield handle02(emp)
        yield func(emp)


for item in select(list_employees, lambda emp: emp.name):
    print(item)
"""

for item in IterableHelper.select(list_employees, lambda emp: emp.name):
    print(item)