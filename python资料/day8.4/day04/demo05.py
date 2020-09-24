"""

"""
# 累加 1--100  能被3整除的整数
# sum_value = 0
# for number in range(1, 101):
#     # 思路:满足条件  干
#     if number % 3 == 0:
#         sum_value += number
# print(sum_value)

sum_value = 0
for number in range(1, 101):
    # 思路:不满足条件  跳
    if number % 3 != 0:
        continue  # 跳过  - 继续执行下次循环
        # break# 跳出 - 打断/中断
    sum_value += number
print(sum_value)
