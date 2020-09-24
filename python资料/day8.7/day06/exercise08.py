"""
    定位练习：
        在终端中打印香港的现有人数
        在终端中打印辽宁的新增和现有人数
        新疆新增人数增加1
    删除练习：
        删除香港现有人数信息
        删除新疆新增人数信息
        删除辽宁的新增和现有信息
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

print(dict_HongKong["now"])
print(dict_LiaoNing["new"])
print(dict_LiaoNing["now"])
# dict_XinJiang["new"] = dict_XinJiang["new"] + 1
dict_XinJiang["new"] += 1

del dict_HongKong["now"]
del dict_XinJiang["new"]
del dict_LiaoNing["now"]
del dict_LiaoNing["new"]