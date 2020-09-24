from common.iterable_tools import IterableHelper
# 要求：通过IterableHelper类实现

# lamdba 参数是列表中的元素

list01 = [4, 5, 65, 76, 87, 98]
# 练习1：在list01中查找第一个奇数
print(IterableHelper.find_single(list01,lambda number:number % 2))

# 练习2：在list01中查找大于10的数字总和
print(IterableHelper.get_count(list01,lambda item:item > 10))

# 练习3：在dict01中查找value大于1001的所有key
dict01 = {"张无忌": 1001, "赵敏": 1002, "周芷若": 1003}
for item in IterableHelper.find_all(dict01,lambda key:dict01[key] > 1001):
    print(item)