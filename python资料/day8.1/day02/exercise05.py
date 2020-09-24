"""
    在终端中获取商品单价、购买的数量和支付金额。
    计算应该找回多少钱。
"""
# 获取数据 - 单价  数量 金额
unit_price = int(input("请输入单价:"))
quantity = int(input("请输入数量:"))
money = float(input("请输入金额:"))
# 逻辑计算 - 金额 - 单价 * 数量
result = money - unit_price * quantity
# 显示结果 - 应找回:xx元
print("应找回:" + str(result) + "元")
