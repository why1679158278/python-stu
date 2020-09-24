"""
    类型间转换
        结果 = 类型名称(数据)
    练习:exercise05

"""
# 1. 引入
# 获取的数据永远都是字符串类型
# str_age = input("请输入年龄：")#  "16"  -->  16
# int_age = int(str_age)
# # "格式" + str(数)
# print("您明年" + str(int_age + 1))

# 2. 各种类型互相转换
# str  ->  int
data01 = int("16")
# int  ->  str
data02 = str(16)

# str  ->  float
data03 = float("16.5")
# float  ->  str
data04 = str(16.5)

# int  -> float
data05 = float(250)
# float  -> int
data06 = int(2.1)  # 向下取整 2
print(data06)

# 3. 如果str -> 其他类型,那么必须是该类型的字符串表达形式
# data07 =int("2.1") # 报错
# data07 =float("asdf") # 报错
data08 = float("100")  # 100.0
print(data08)
