"""
    古代的秤，一斤十六两。
    在终端中获取两，计算几斤零几两。
"""
total_liang = int(input("请输入两:"))
jin = total_liang // 16
liang = total_liang % 16
print(str(jin) + "斤零" + str(liang) + "两")
