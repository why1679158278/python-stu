


# 练习1： 将列表中所有奇数设置为None
list01 = [43, 4, 54, 56, 67, 78]
for i, item in enumerate(list01):
    if item % 2:
        list01[i] = None
print(list01)

# 练习2： 打印键值对的同时,打印索引
# 格式：  索引  键  值
dict01 = {"a": "A", "b": "B"}
# for index, item in enumerate(dict01.items()):
#     print(index, item[0], item[1])

for index, (key, value) in enumerate(dict01.items()):
    print(index, key, value)
