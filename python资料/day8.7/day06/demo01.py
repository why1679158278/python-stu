"""
    list -- > str
    将多个字符串拼接为一个。
	result = "连接符".join(列表)

"""
list01 = ["a", "b", "c"]
result = "#".join(list01)
print(result)

# 需求：根据xx逻辑循环拼接字符串
# result = ""
# for number in range(10):  # 0~9
#     # 每次循环  创建新字符串  产生一个垃圾
#     result += str(number)  # "1"  + "2"  -> "12"
# print(result)

# 核心思想：用可变对象代替不可变对象
result = []
for number in range(10):  # 0~9
    # 每次追加都在原列表基础上,没有创建新列表
    result.append(str(number))
result = "".join(result)
print(result)
