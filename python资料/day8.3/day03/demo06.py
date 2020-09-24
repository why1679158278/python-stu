"""
    while
        while True:
            循环体
            if 退出条件:
                break
    练习:exercise09
"""

# 死循环
while True:
    if float(input("请输入您的存款")) > 100000:
        print("娶你")
    else:
        print("学习")

    if input("请输入q退出:") == "q":
        break
