# 使用列表推导式
# 生成1--50之间能被3或者5整除的数字
# 生成5 -- 100之间的数字平方

# list_result = []
# for number in range(1, 51):
#     if number % 3 == 0 or number % 5 == 0:
#         list_result.append(number)

list_result = [number for number in range(1, 51) if number % 3 == 0 or number % 5 == 0]
print(list_result)

list_result = [number ** 2 for number in range(5, 101)]
print(list_result)
