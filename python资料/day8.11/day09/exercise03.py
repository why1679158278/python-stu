"""
    参照day07/demo08
    定义函数,对列表进行降序排列.
"""


# list01 = [5, 15, 25, 35, 1, 2]
# for r in range(len(list01) - 1):
#     for c in range(r + 1, len(list01)):
#         if list01[r] < list01[c]:
#             list01[r], list01[c] = list01[c], list01[r]
# print(list01)


def descending_order(list_target):
    # 2. 修改可变
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] < list_target[c]:
                list_target[r], list_target[c] = list_target[c], list_target[r]
    # 3. 无需通过return返回
    # return list_target

# 1. 传入可变
list01 = [5, 15, 25, 35, 1, 2]
# result = descending_order(list01)
# print(result)
descending_order(list01)
print(list01)