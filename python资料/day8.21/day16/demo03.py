"""
    列表推导式
        结果 = [变量 for 变量 in 可迭代对象 if 条件]
        结果是列表(数据)

    生成表达式
       结果 = (变量 for 变量 in 可迭代对象 if 条件)
       结果是生成器(推算数据)
"""
# list_result = []
# for item in range(1,10):
#     if item % 2:
#         list_result.append(item)

# 构建列表的简化写法
list_result = [item for item in range(1, 10) if item % 2]
for number in list_result:
    print(number)

# def get_numbers():
#     for item in range(1, 10):
#         if item % 2:
#             yield item
#
# generator = get_numbers()
# for number in generator:
#     print(number)

generator = (item for item in range(1, 10) if item % 2)
for number in generator:
    print(number)


