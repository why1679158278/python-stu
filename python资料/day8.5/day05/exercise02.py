"""
    1.
        创建列表,存储3个数据
            地区列表
            新增列表
            现有列表
    2.
        向以上三个列表追加数据,
        在第1个位置插入数据
"""
list_region = ["香港", "新疆", "辽宁"]
list_new = [80, 22, 0]
list_now = [1486, 618, 93]

list_region.append("台湾")
list_region.insert(0,"广东")

list_new.append(2)
list_new.insert(0,0)

list_now.append(28)
list_now.insert(0,18)

print(list_region)
print(list_new)
print(list_now)