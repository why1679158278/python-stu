"""
    生成器应用
    定义函数,在列表中找出所有大于10的数字
"""


# 传统思想：用容器存储所有结果
# def find_numbers_gt_10(list_target):
#     list_result = []
#     for item in list_target:
#         if item > 10:
#             list_result.append(item)
#     return list_result
#
# list01 = [43,54,566,7,6,8]
# result = find_numbers_gt_10(list01)
# for item in result:
#     print(item)

# 生成器思想：循环一次  计算一次  返回一次
def find_numbers_gt_10(list_target):
    for item in list_target:
        if item > 10:
            yield item


list01 = [43, 54, 566, 7, 6, 8]
result = find_numbers_gt_10(list01)
for item in result:
    print(item)
