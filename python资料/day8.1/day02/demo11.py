"""
    bool 类型操作(2)
        逻辑运算符
            判断多个命题之间的关系
    练习:exercise10
"""
# 与
# 并且   都满足 结果 才满足
print(True and True)  # True
print(False and True)  # False
print(True and False)  # False
print(False and False)  # False

#
# 来自于丈母娘的灵魂质问
# 命题: 有钱  并且  有房
# float(input("请输入您的存款")) > 100000
# input("请输入您是否有房") == "有"
#
# print(float(input("请输入您的存款")) > 100000 and input("请输入您是否有房") == "有")


# 或
# 或者   有一个满足 结果 才满足
print(True or True)  # True
print(False or True)  # True
print(True or False)  # True
print(False or False)  # False

# 命题: 有钱  或者  有房
print(float(input("请输入您的存款")) > 100000
      or input("请输入您是否有房") == "有")

# 非
# 取反
print(not True)

# 练习:
# 年龄大于25 并且 身高小于170
# 职位是高管 或者 年薪大于500000
