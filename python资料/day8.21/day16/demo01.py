"""
    内置生成器
        enumerate
"""
list01 = [43, 54, 5, 6, 67, 78, 9]
# # 从头到尾 依次 读取数据
# for item in list01:
#     # print(item)
#     item = 0
#
for i in range(len(list01)):
    list01[i] = 0
    # print(list01[i])

# enumerate 生成的是元组(索引,元素)
# 从头到尾 依次 操作数据(能读能写)
for i, item in enumerate(list01):
    if item > 10:
        list01[i] = 0
