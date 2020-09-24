"""
    在终端中循环录入商品信息(名称,价格),
    当商品名称为空时停止录入。
    判断如果录入了"屠龙刀",那么将其删除.
    按格式打印所有信息：xx的价格是xx.
"""
dict_commoditys = {}
while True:
    commodity_name = input("请输入商品名称：")
    if commodity_name == "":
        break
    commodity_price = int(input("请输入商品价格："))
    dict_commoditys[commodity_name] = commodity_price

if "屠龙刀" in dict_commoditys:
    del dict_commoditys["屠龙刀"]

for key, value in dict_commoditys.items():
    print(f"{key}的价格是{value}.")
