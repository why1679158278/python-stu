"""
    遍历练习：
        在终端中打印dict_HongKong所有键(一行一个)
        在终端中打印dict_XinJiang所有值(一行一个)
        在终端中打印dict_LiaoNing所有键和值(一行一个)
        在dict_LiaoNing字典中查找93对应的键名称
"""

dict_HongKong = {"region": "香港", "new": 80, "now": 1486}

dict_XinJiang = {
    "region": "新疆",
    "new": 22,
    "now": 618
}

dict_LiaoNing = {
    "region": "辽宁",
    "new": 0,
    "now": 93
}

for key in dict_HongKong:
    print(key)

for value in dict_XinJiang.values():
    print(value)

for key, value in dict_LiaoNing.items():
    print(key)
    print(value)

for key, value in dict_LiaoNing.items():
    if value == 93:
        print(key)
