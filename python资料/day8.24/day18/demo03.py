"""
    闭包应用
        价值：逻辑连续
        案例：从得到500元压岁钱,到不断购买新商品的过程
             能够连续,不中断.
"""


# 压岁钱
def give_gife_money(money):
    """
        获取压岁钱
    """
    print(f"获取{money}元压岁钱")

    def child_buy(commodity, price):
        """
            孩子购买商品
        """
        nonlocal money
        money -= price
        print(f"孩子购买{commodity}商品,花了{price},还剩下{money}元")

    return child_buy


action = give_gife_money(500)
action("变形金刚", 150)
action("芭比娃娃", 250)
action("天线宝宝", 50)
