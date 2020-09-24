"""
re功能扩展标志
"""
import re

# 目标字符串
s = """Hello 
北京
"""
# 让 ^ $ 代表每一行的开头结尾位置
result = re.findall(r"^.+",s,re.M|re.A)
print(result)


# 让 . 可以匹配换行
# result = re.findall(r".+",s,re.S)
# print(result)


# 让元字符只能匹配英文字符
# result = re.findall(r"\w+",s,re.A)
# print(result)


# 匹配不区分字母大小写
# result = re.findall(r"[a-z]+",s,re.I)
# print(result)










