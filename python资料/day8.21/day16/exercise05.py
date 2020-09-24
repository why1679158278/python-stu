"""
    参照demo05
    定义函数，在列表中查找奇数
    定义函数，在列表中查找能被3或5整除的数字
    步骤：
        1. 根据需求，创建函数。
        2. 分
        3. 隔
        4. 做  不变的+变化的

    练习：
        将find_all函数定义到
        common/iterable_tools模块的IterableHelper类中
        在当前模块中通过类名调用
"""
from common.iterable_tools import IterableHelper


def find_all_odd(list_target):
    for number in list_target:
        if number % 2:
            yield number


def find_all_number(list_target):
    for number in list_target:
        if number % 3 == 0 or number % 5 == 0:
            yield number


list01 = [43, 342, 54, 56, 6, 67]
for item in find_all_odd(list01):
    print(item)


# 1. 分
# -- 变化的
def condition01(number):
    return number % 2


def condition02(number):
    return number % 3 == 0 or number % 5 == 0


# -- 不变的
def find_all(list_target, func):
    for number in list_target:
        # if number % 3 == 0 or number % 5 == 0:
        # if condition02(number):
        if func(number):
            yield number


# 好处：再增加条件，find_all不变
list01 = [4, 5, 65, 76, 87, 98]
for item in find_all(list01, condition02):
    print(item)



for item in IterableHelper.find_all(list01, condition02):
    print(item)