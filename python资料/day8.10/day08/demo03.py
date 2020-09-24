"""
    返回值
        函数的结果
        def 函数名():
            ....
            return 数据

        变量　= 函数名()
"""


# 创建美元转换为人民币的函数
def usd_to_cny(usd):
    """
        美元转换为人民币
    :param usd: 美元
    :return:人民币
    """
    # 2. 逻辑处理 - 美元 * 6.99
    cny = usd * 6.99
    return cny  # 给


# 收
result = usd_to_cny(5)
print(result)
