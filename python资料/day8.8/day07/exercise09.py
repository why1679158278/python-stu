# 练习：升序排列 ： 小 --> 大
list01 = [5, 1, 5, 5, 2, 23, 55, 4]
# 1. 取数据
for r in range(len(list01) - 1):
    # 2. 作比较
    for c in range(r + 1, len(list01)):
        if list01[r] > list01[c]:
            list01[r], list01[c] = list01[c], list01[r]
print(list01)