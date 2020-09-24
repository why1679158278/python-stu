"""
    定义函数,在终端中打印一维列表.
"""


# 做法　＋　用法
# list01 = [5, 546, 6, 56, 76, ]
# for item in list01:
#     print(item)
#
# list02 = [7,6,879,9,909,]
# for item in list02:
#     print(item)

def print_single_list(list_target):
    for item in list_target:
        print(item, end=" ")
    print()


list01 = [5, 546, 6, 56, 76, ]
print_single_list(list01)

list02 = [7, 6, 879, 9, 909, ]
print_single_list(list02)
