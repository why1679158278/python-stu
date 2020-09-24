"""
    全局变量与局部变量
"""

a = 10


def func01():
    # 在函数内部,只能读取全局变量
    a = 20  # 创建局部变量,没有修改全局变量
    print(a)  # 20


func01()
print(a)  # 10


def func02():
    global a  # 如果在局部变量修改全局变量,必须通过global声明
    a = 20
    print(a)


func02()
print(a)


# 注意:
c = [10]
def func03():
    c[0] = 20  # 没有修改全局变量c(修改的的是列表的元素)
    print(c)  # [20]


func03()
print(c)  # [10]
