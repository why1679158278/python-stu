"""
    需求：定义函数，获取钱最多的员工
         定义函数，获取员工编号最大的员工
    目标:定义通用的,获取最大值函数.
    温馨提示：只能获取最大值,不具备获取最小值.
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
# list01 = [4, 54, 5, 65, 76]
# def get_max(list_target):
#     max_value = list_target[0]
#     for i in range(1, len(list_target)):
#         if max_value < list_target[i]:
#             max_value = list_target[i]
#     return max_value
# print(get_max(list01))


def get_max_by_money(list_target):
    max_value = list_target[0]
    for i in range(1, len(list_target)):
        if max_value.money < list_target[i].money:
            max_value = list_target[i]
    return max_value


def get_max_by_eid(list_target):
    max_value = list_target[0]
    for i in range(1, len(list_target)):
        if max_value.eid < list_target[i].eid:
            max_value = list_target[i]
    return max_value


print(get_max_by_money(list_employees).__dict__)


def get_max(list_target, func):
    max_value = list_target[0]
    for i in range(1, len(list_target)):
        # 原来"我自己点money"
        # if max_value.money < list_target[i].money:
        # 现在"我交给你(参数)点money"
        if func(max_value) < func(list_target[i]):
            max_value = list_target[i]
    return max_value


print(get_max(list_employees, lambda emp: emp.money).__dict__)

"""

print(IterableHelper.get_max(list_employees, lambda emp: emp.money).__dict__)

