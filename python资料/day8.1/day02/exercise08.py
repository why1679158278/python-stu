"""
    在终端中录入一个4位整数, 打印每位相加和
    例如：1234 -->  1 + 2+ 3 + 4
"""
number = int(input("请输入4位整数:"))
# 写法1
# unit01 = number % 10
# # 1234 // 10 --> 123 % 10 --> 3
# unit02 = number // 10 % 10
# # 1234 // 100 --> 12 % 10 --> 2
# unit03 = number // 100 % 10
# unit04 = number // 1000
# result = unit01 + unit02 + unit03 + unit04

# 写法2(建议)
result = number % 10  # 个位
# 累加：在原来基础上增加
result += number // 10 % 10  # 累加十位
result += number // 100 % 10  # 累加百位
result += number // 1000  # 累加千位
print("结果是:" + str(result))