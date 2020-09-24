"""
    1.
        在终端中录入一个整数，
        如果是奇数为变量state赋值"奇数",
        否则赋值"偶数"。
"""
number = int(input("请输入数字:"))
# if number % 2 != 0: #　　有值
# if number % 2:  # bool(number % 2)    有值
#     state = "奇数"
# else:
#     state = "偶数"

state ="奇数" if number % 2 else "偶数"
print(state)
