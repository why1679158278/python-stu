"""
    day11/homework/exercise02
    练习：查找部门编号是9001的所有员工
    分别使用生成器函数 与 生成器表达式 实现

    适用性：
        生成器函数,擅长重复使用,通常给其他人使用.
        生成器表达式,不能重复使用,通常自己使用.
"""
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



def find_employee_by_did():
    for emp in list_employees:
        if emp.did == 9001:
            yield emp

# 创建生成器对象
result = find_employee_by_did()
# 推算数据
for item in result:
    print(item.__dict__)

result = find_employee_by_did()
# 推算数据
for item in result:
    print(item.__dict__)

# 创建生成器对象
generator_result = (emp for emp in list_employees if emp.did == 9001)
# 推算数据
for item in generator_result:
    print(item.__dict__)

# 推算数据(不能使用)
for item in generator_result:
    print(item.__dict__)

