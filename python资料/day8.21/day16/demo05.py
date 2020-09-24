"""
    函数式编程思想：
        分：将变化点单独定义到函数中
        隔：用参数在不变的代码中,调用变化的函数
        做：以参数的调用方式为规定，制作变化函数。

    适用性：
        好多相似的代码,但核心算法不同.
    参数：
        传递列表视为数据(名词)灵活
        传递函数视为逻辑(动词)灵活
"""


# 定义函数,在列表中查找所有偶数
from common.iterable_tools import IterableHelper


def find_all_even(list_target):
    for item in list_target:
        if item % 2 == 0:
            yield item

# 定义函数,在列表中查找所有小于10的数字
def find_all_lt_10(list_target):
    for item in list_target:
        if item < 10:
            yield item

list01 = [42, 43, 5, 65, 6, 78]
for number in find_all_even(list01):
    print(number)

# 1. 分
# -- 将变化的单独定义到函数中
def condition01(item):
    return item % 2 == 0

def condition02(item):
    return item < 10

# -- 将不变的单独定义到函数中
def find_all(list_target,func):# 2. 隔 func
    for item in list_target:
        # if item % 2 == 0:
        # if condition01(item):
        # if condition02(item):
        if func(item):
            yield item

# 3. 做 func
# 将变化的 与 不变的 相结合
for item in find_all(list01,condition01):
    print(item)

# 因为先在find_all中确定了用法(一个参数)
# 所以condition03不能传入到find_all中
# def condition03(a,b):
#     return a > b
#
# for item in find_all(list01,condition03):
#     print(item)


for item in IterableHelper.find_all(list01,condition01):
    print(item)