"""
    装饰器
        不改变原函数   增加新功能

        有外有内:外在接收旧功能,内在包裹旧与新功能
        内访问外：将新功能与旧功能同时执行
        外返回内：让其他代码重复使用内部函数
"""


def new_func(func):
    # 包裹:新功能 + 旧功能
    def wrapper():
        print("新功能")  # 执行新功能
        func()  # 调用旧功能

    return wrapper


# def new_func():
#     print("新功能")

def func01():
    print("func01执行喽")


@new_func  # func02 = new_func(func02)
def func02():
    print("func02执行喽")

# 拦截 = 新功能 + 旧功能
# 调用外函数,传递旧功能,返回内(包裹)函数
func01 = new_func(func01)

# 调用内部函数
func01()
func02()
