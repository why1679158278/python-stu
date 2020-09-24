"""
    类成员
        类变量:大家的数据
            创建：
                在类中,方法外
                    变量名 = 数据
            使用：
                通过类名访问
                    类名.变量名
        类方法:操作类变量
            创建：
                @classmethod
                def 方法名(cls,参数):
                    方法体
            使用：
                通过类名访问
                    类名.方法名(参数)
"""


class ICBC:
    """
        工商银行
    """
    # 类变量：总行的钱
    total_money = 1000000
    # 类方法：操作类变量
    @classmethod
    def print_total_money(cls):
        # print("总行的钱：", ICBC.total_money)
        print("总行的钱：", cls.total_money)
    def __init__(self, money=0):
        # 实例变量：支行的钱
        self.money = money
        # 总行的钱因为创建一家支行而减少
        ICBC.total_money -= money
ttzh = ICBC(100000)
trtzh = ICBC(200000)
# print("总行的钱：", ICBC.total_money)

ICBC.print_total_money()
