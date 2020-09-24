"""
    返回值　－　语法　
"""


# 1. python中函数默认返回None
def func01():
    print("func01执行了")
    # return None


result = func01()
print(result)  # None

# 2.python中return后面没有数据,默认为None
def func02():
    print("func02执行了")
    return

result = func02()
print(result)  # None

# 3. return可以退出函数(无论多少层循环嵌套,都可以)
def func03():
    print("func03执行了")
    return
    print("func03又执行了")

func03()
