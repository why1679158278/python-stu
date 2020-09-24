"""
    创建商品列表
    在商品列表中查找是否存在Commodity(name="屠龙刀") in
    在商品列表中查找Commodity(name="口罩")的数量  count
    根据单价对商品升序排列      sort
    查找单价最低的商品   min
"""


class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.price < other.price


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]

print(Commodity(name="屠龙刀") in list_commodity_infos)

print(list_commodity_infos.count(Commodity(name="口罩")))

list_commodity_infos.sort()

min_by_price = min(list_commodity_infos)
print(min_by_price)

print(list_commodity_infos)