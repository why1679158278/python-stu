"""
    在终端中获取一个整数，作为边长，打印矩形。
"""
number = int(input("请输入整数:"))  # 5
for row in range(number):
    if row == 0 or row == number - 1:
        print("*" * number)# 打印头尾
    else:# 打印中间
        # print("*" + " " * (number - 2) + "*")
        print("*%s*" % (" " * (number - 2)))
