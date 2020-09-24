"""
    定义函数,将列表中大于某个值的元素设置为None
        参数               结果
    list01   10 -->  [None,None,None,7,None,8]
    list01   100 -->  [34,None,56,7,78,8]
"""


def set_none_gt_number(list_target, number):
    # 函数内部修改了传入的可变对象,所以不用通过return返回结果
    for i in range(len(list_target)):
        if list_target[i] > number:
            list_target[i] = None


list01 = [34, 545, 56, 7, 78, 8]
set_none_gt_number(list01, 10)
print(list01)# [None, None, None, 7, None, 8]

