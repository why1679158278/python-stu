"""
    列表推导式
    字典推导式
        根据可迭代对象,创建容器时,使用推导式
"""
# 需求：key:1-10    value: key的平方
# dict_result = {}
# for number in range(1,11):
#     dict_result[number] = number ** 2

dict_result = {number: number ** 2 for number in range(1, 11)}
print(dict_result)

# dict_result = {}
# for number in range(1,11):
#     if number % 2 == 0:
#         dict_result[number] = number ** 2
dict_result = {number:number ** 2 for number in range(1,11) if number % 2 == 0}
print(dict_result)
