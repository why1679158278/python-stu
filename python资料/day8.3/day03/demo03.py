"""
   选择语句
        让语句有选择性的执行
        if 条件1:
            满足条件1执行的代码
        elif 条件2:
            不满足条件1,但是满足条件2执行的代码
        else:
            不满足以上条件执行的代码
    练习:exercise02~06
"""
# 满足条件 -> 娶你
#  否则 -> 学习
number = int(input("请输入数字:"))
if number > 0:
    print("正数")
elif number < 0:
    print("负数")
else:
    print("0")
