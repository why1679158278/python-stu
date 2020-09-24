"""
    自定义排序算法
        降序排列 ： 大 --> 小
        升序排列 ： 小 --> 大

        算法：
            取出第一个数据,与后面元素进行比较,发现更大/更小,则交换.
            取出第二个数据,与后面元素进行比较,发现更大/更小,则交换.
            取出第三个数据,与后面元素进行比较,发现更大/更小,则交换.
                 ...
               倒数第二个
"""
list01 = [5, 15, 25, 35, 1, 2]
# 第一个位置是最大元素
# for i in range(1, len(list01)):
#     if list01[0] < list01[i]:
#         list01[0], list01[i] = list01[i], list01[0]
# 第二个位置是最大元素
# for i in range(2, len(list01)):
#     if list01[1] < list01[i]:
#         list01[1], list01[i] = list01[i], list01[0]
# .....
# 取数据：前几个数据(不要最后一个)
for r in range(len(list01) - 1):
    # 作比较：用取出的数据与后面的数据进行比较
    for c in range(r + 1, len(list01)):
        if list01[r] < list01[c]:
            list01[r], list01[c] = list01[c], list01[r]
print(list01)
