"""
    lambda练习
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


# 练习1：调用使用lambda代替condition01
# 参照day16/exercise05
def condition01(number):
    return number % 3 == 0 or number % 5 == 0


list01 = [4, 5, 65, 76, 87, 98]
# for item in IterableHelper.find_all(list01, condition01):
#     print(item)

for item in IterableHelper.find_all(list01, lambda number: number % 3 == 0 or number % 5 == 0):
    print(item)


# 练习2：调用使用lambda代替condition02
def condtion02(item):
    return item.name == "沙僧"


# print(IterableHelper.find_single(
#     list_employees, condtion02).__dict__)

print(IterableHelper.find_single(
    list_employees, lambda item: item.name == "沙僧").__dict__)

# 练习3： 打印字典中所有姓名大于2个字的人名
dict01 = {"张无忌": 1001, "赵敏": 1002, "周芷若": 1003}
# for key in dict01:
#     if len(key) > 2:
#         print(key)
for item in IterableHelper.find_all(dict01,
                                    lambda key: len(key) > 2):
    print(dict01[item])
