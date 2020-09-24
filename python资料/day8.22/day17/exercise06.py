"""
    需求1：
        定义函数,删除工资大于20000的所有员工
        定义函数,删除部门编号是9001的所有员工
    需求2：
        定义函数,根据工资对员工列表进行排序(升序)
        定义函数,根据部门编号对员工列表进行排序(升序)
        温馨提示：只能升序,不支持降序
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
# 定义函数,删除工资大于20000的所有员工
# 定义函数,删除部门编号是9001的所有员工
# list01 = [43, 14, 5, 6, 76, 78]
#
# def delete_all_gt_10(list_target):
#     count = 0
#     for i in range(len(list_target) - 1, -1, -1):
#         if list_target[i] > 10:
#             del list_target[i]
#             count += 1
#     return count
#
# print(delete_all_gt_10(list01))
# print(list01)

def delete_all_by_money(list_target):
    count = 0
    for i in range(len(list_target) - 1, -1, -1):
        if list_target[i].money > 20000:
            del list_target[i]
            count += 1
    return count

def delete_all_by_did(list_target):
    count = 0
    for i in range(len(list_target) - 1, -1, -1):
        if list_target[i].did == 9001:
            del list_target[i]
            count += 1
    return count

def delete_all(list_target,func):
    count = 0
    for i in range(len(list_target) - 1, -1, -1):
        # if list_target[i].money > 20000:
        if func(list_target[i]):
            del list_target[i]
            count += 1
    return count

print(delete_all(list_employees,lambda emp:emp.money > 20000))
print(list_employees)
"""

print(IterableHelper.delete_all(list_employees, lambda emp: emp.money > 20000))


# list01 = [43, 14, 5, 6, 76, 78]
# def order_by(list_target):
#     for r in range(len(list_target) - 1):
#         for c in range(r + 1, len(list_target)):
#             if list_target[r] > list_target[c]:
#                 list_target[r], list_target[c] = list_target[c], list_target[r]
#
# order_by(list01)
IterableHelper.order_by(list_employees,lambda emp:emp.money)
print(list_employees)
