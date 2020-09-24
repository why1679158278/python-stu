# 参照day02/exercise06代码
# 定义函数,根据总两数,计算几斤零几两.
# 提示：使用容器包装需要返回的多个数据

# total_liang = int(input("请输入两:"))
# jin = total_liang // 16
# liang = total_liang % 16
# print(str(jin) + "斤零" + str(liang) + "两")

# 崇尚小而精,拒绝大而全.
def get_weight(total_liang):
    """
        根据总重量获取斤两
    :param total_liang:总重量
    :return:元组类型(斤,两)
    """
    jin = total_liang // 16
    liang = total_liang % 16
    return jin, liang


# result = get_weight(100)
# print(result[0])
# print(result[1])
jin, liang = get_weight(100)
print(str(jin) + "斤零" + str(liang) + "两")
