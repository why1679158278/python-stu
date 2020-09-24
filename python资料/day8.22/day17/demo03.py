"""
    内置高阶函数
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

# 1. 映射 map
# 需求：获取所有员工的姓名
# for name in IterableHelper.select(list_employees,lambda emp:emp.name):
#     print(name)
for name in map(lambda emp: emp.name, list_employees):
    print(name)

# 2. 过滤filter
# 需求：获取工资大于20000的所有员工
# for item in IterableHelper.find_all(list_employees,lambda emp:emp.money > 20000):
#     print(item.__dict__)
for item in filter(lambda emp: emp.money > 20000, list_employees):
    print(item.__dict__)

# 3. max/min
# 需求：获取最有钱的人
print(max(list_employees, key=lambda emp: emp.money).__dict__)

# 4. 排序
# 备注：返回新列表,没有修改原有可迭代对象

# 需求：根据钱升序
# IterableHelper.order_by(list_employees, lambda emp: emp.money)
# print(list_employees)
result = sorted(list_employees,key = lambda emp: emp.money)
print(result)

# 需求：根据钱降序
result = sorted(list_employees,key = lambda emp: emp.money,reverse=True)
print(result)



