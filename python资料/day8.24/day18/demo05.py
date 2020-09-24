"""
    装饰器 语法细节
        内部函数的返回值:旧功能的返回值
"""


def new_func(func):
    # 多个实参 合为 一个元组(args)一个字典(kwargs)
    def wrapper(*args, **kwargs):
        print("新功能")
        # 一个元组(args)一个字典(kwargs) 拆为 多个实参
        result = func(*args, **kwargs)  # 调用旧功能,获取返回值
        return result  # 内部函数返回旧功能的返回值

    return wrapper


@new_func
def func01(a):
    print("func01执行喽,参数是：", a)
    return 100


@new_func
def func02(b, c):
    print("func02执行喽,参数是", b, c)
    return "ok"

# 调用的是内部函数
re01 = func01(1)
re02 = func02(2, 3)
re02 = func02(b=20, c=30)
re02 = func02(200, c=300)
print(re01)  # 100
print(re02)  # ok
