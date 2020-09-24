"""
    参照day05/exericse02
    1.
        创建字典,存储3个地区疫情信息（地区/新增/现有）
    2.
        向以上三个字典追加累计信息,
            "香港", "新疆", "辽宁"
            3849    799   259
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

dict_HongKong["total"] = 3849
dict_XinJiang["total"] = 799
dict_LiaoNing["total"] = 259
