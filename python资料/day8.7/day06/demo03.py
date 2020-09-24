"""
    列表推导式
        使用简易方式创建列表
            [操作变量 for 变量 in 可迭代对象 if 条件]
"""
# list_result = []
# for number in range(1,11):
#     if number % 2:
#         list_result.append(number)

list_result = [number for number in range(1, 11)
               if number % 2]
print(list_result)
# list_result = []
# for number in range(1,11):
#         list_result.append(number ** 2)
list_result = [number ** 2 for number in
               range(1, 11)]
