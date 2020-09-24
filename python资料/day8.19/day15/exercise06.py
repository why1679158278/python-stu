"""
    迭代器版本的商品管理器 改为 yield版本
"""

class CommodityController:
    def __init__(self):
        self.__list_commoditys = []

    def add_commodity(self, stu):
        self.__list_commoditys.append(stu)

    def __iter__(self):
        for commodity in self.__list_commoditys:
            yield commodity

controller = CommodityController()
controller.add_commodity("屠龙刀")
controller.add_commodity("倚天剑")
controller.add_commodity("芭比娃娃")

for item in controller:
    print(item)