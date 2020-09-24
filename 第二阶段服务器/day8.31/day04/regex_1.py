"""
re 模块基础示例
"""
import re

# 目标字符串
s = "Alex:2000,Sunny:1999"
pattern = r"(?P<name>\w+):(\d+)"

# 使用## 替换正则表达式匹配到的内容
result = re.sub(r"\W+","##",s,2)
print(result)


# 使用正则表达式匹配到的内容分割目标字符串
# result = re.split("\W+",s,2)
# print(result)


# 正则表达式中有子组，则只能返回子组对应部分
# result = re.findall(pattern,s)
# print(result)