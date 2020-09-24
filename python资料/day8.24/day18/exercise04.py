"""
    为sum_data,增加打印函数执行时间的功能.

    函数执行时间
        公式： 执行后时间 - 执行前时间
        技术：time.time()
"""
import time


def print_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        # 执行旧功能
        result = func(*args, **kwargs)
        stop = time.time()
        print(f"执行时间是：{stop - start}")
        return result

    return wrapper


@print_execution_time
def sum_data(n):
    sum_value = 0
    for number in range(n):
        sum_value += number
    return sum_value


print(sum_data(10))
print(sum_data(1000000))
