"""
re 模块基础示例2
"""
import re

# 目标字符串
s = "Alex:2000,Sunny:1999"
pattern = r"(?P<name>\w+):(\d+)"

# 匹配开头位置
# result = re.match(pattern,s)
# print(result.group())

# 只匹配第一处
result = re.search(pattern,s)
print(result.groupdict())

# 匹配目标得到迭代对象
# result = re.finditer(pattern,s)
#
# for i in result:
#     # 迭代取值，取出的i是match对象
#     print(i.span()) # 获取匹配内容的位置
#     print(i.group())  # 获取匹配内容
#     # 通过组名和序号都可以获取子组对应内容
#     print(i.group('name'),'--',i.group(2))






