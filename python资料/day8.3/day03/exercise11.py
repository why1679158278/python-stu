"""
    在终端中循环录入年龄,
    如果录入空,则退出循环.
    最后打印平均年龄(总年龄除以人数)
"""
sum_age = 0
count = 0
while True:
    str_age = input("请输入年龄:")
    if str_age == "":
        break  # 退出循环
    # 如果不是空,才会执行下列代码
    age = int(str_age)
    sum_age += age
    count += 1
print(sum_age / count)
