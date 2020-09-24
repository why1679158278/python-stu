"""
    使用闭包模拟以下情景：
    在银行开户存入10000
    购买xx商品花了xx元
    购买xx商品花了xx元
"""


def open_bank_account(money):
    print("开户存入%d元" % money)

    def buy(commodity, price):
        nonlocal money
        money -= price
        print("购买%s商品花了%d元"%(commodity,price))

    return buy

# 调用外,得到内
action = open_bank_account(10000)
# 调用内
action("羊肉串",100)
action("大腰子",300)


