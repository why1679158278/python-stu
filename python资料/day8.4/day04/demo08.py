"""
    字符串字面值
"""
# 写法1:单引号
content01 = '我爱编程'
# 写法2:双引号
content02 = "我爱编程"
# 写法3:三引号
# -- 可见即所得
content03 = '''
我  爱
     编    程'''
print(content03)
content03 = """我爱编程"""

# 解决冲突问题方案1:
content04 = '我爱"Python"编程'
content05 = "我爱'Python'编程"
content06 = """我爱'P'yth"on"编程"""

# 解决冲突问题方案2:
#   -- 转义字符:改变原始含义的特殊字符
#       \"   \n换行    \\   r"...."原始字符
content06 = "我爱\"Python\"编程"
print(content06)

# 路径: \\
url = "C:\\nRIVERS\\bMDVGA\\driver\\Images"
url = r"C:\nRIVERS\bMDVGA\driver\Images"
print(url)

