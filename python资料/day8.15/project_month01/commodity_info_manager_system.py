"""
    商品信息管理系统
"""


class CommodityModel:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price


class CommodityView:
    """
        商品界面视图
            负责处理界面逻辑(输入/输出)
    """

    def __init__(self):
        self.__controller = CommodityController()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("1. 添加商品信息")
        print("2. 显示商品信息")
        print("3. 删除商品信息")
        print("4. 修改商品信息")

    def __select_menu(self):
        item = input("请输入您的选项：")
        if item == "1":
            self.__input_commodity()
        elif item == "2":
            self.__display_commoditys()
        elif item == "3":
            self.__delete_commodity()
        elif item == "4":
            self.__change_commodity()

    def __input_commodity(self):
        commodity = CommodityModel()
        commodity.name = input("请输入商品名称：")
        commodity.price = int(input("请输入商品单价："))

        self.__controller.add_commodity(commodity)

    def __display_commoditys(self):
        for commodity in self.__controller.list_commoditys:
            print(commodity.__dict__)

    def __delete_commodity(self):
        cid = int(input("请输入需要删除的商品编号："))
        if self.__controller.remove_commodity(cid):
            print("删除成功")
        else:
            print("删除失败")

    def __change_commodity(self):
        commodity = CommodityModel()
        commodity.cid = int(input("请输入商品编号："))
        commodity.name = input("请输入商品名称：")
        commodity.price = int(input("请输入商品单价："))

        if self.__controller.update_commodity(commodity):
            print("成功")
        else:
            print("失败")


class CommodityController:
    """
        商品控制器
            对商品信息的核心处理逻辑(添加/删除/修改..)
    """

    def __init__(self):
        self.__list_commoditys = []
        self.__start_id = 1000

    @property
    def list_commoditys(self):
        return self.__list_commoditys

    def add_commodity(self, commodity_target):
        """
            添加商品信息
        :param commodity_target:目标商品
        """
        commodity_target.cid = self.__start_id
        self.__start_id += 1
        self.__list_commoditys.append(commodity_target)

    def remove_commodity(self, cid):
        """
            移除商品
        :param cid:商品编号
        :return: 是否移除成功
        """
        for i in range(len(self.__list_commoditys)):
            if self.__list_commoditys[i].sid == cid:
                del self.__list_commoditys[i]
                return True
        return False

    def update_commodity(self, commodity):
        """

        :param commodity:
        :return:
        """
        for com in self.list_commoditys:
            if com.cid == commodity.cid:
                com.name = commodity.name
                com.price = commodity.price
                return True
        return False


# 入口
view = CommodityView()
view.main()
