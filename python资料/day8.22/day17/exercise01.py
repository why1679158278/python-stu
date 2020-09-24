"""
    需求：
        定义函数,在员工列表中查找员工编号是1003的员工
        定义函数,在员工列表中查找姓名是沙僧的员工
    步骤：
        1. 根据需求，写出函数。
        2. 因为主体逻辑相同,核心算法不同.
           所以使用函数式编程思想(分、隔、做)
           创建通用函数.find_single
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

def find_single_by_eid(list_target):
    for item in list_target:
        if item.eid == 1003:
            return item

def find_single_by_name(list_target):
    for item in list_target:
        if item.name == "沙僧":
            return item

print(find_single_by_name(list_employees).__dict__)

def condtion01(item):
    return item.eid == 1003

def condtion02(item):
    return item.name == "沙僧"

def find_single(list_target,func):
    for item in list_target:
        # if item.name == "沙僧":
        # if condtion02(item):
        if func(item):
            return item

print(find_single(list_employees,condtion02).__dict__)

print(IterableHelper.find_single(list_employees, condtion02).__dict__)
