# 1. 定义函数,在列表中找出所有偶数
#    [43,43,54,56,76,87,98]
def find_evens(list_target):
    for item in list_target:
        if item % 2 == 0:
            yield item


list01 = [43, 43, 54, 56, 76, 87, 98]
result = find_evens(list01)
for item in result:
    print(item)


# 2. 定义函数,在列表中找出所有数字
#    [43,"悟空",True,56,"八戒",87.5,98]
def find_number(list_target):
    for item in list_target:
        if type(item) == int or type(item) == float:
            yield item


list02 = [43, "悟空", True, 56, "八戒", 87.5, 98]
result = find_number(list02)
for item in result:
    print(item)
