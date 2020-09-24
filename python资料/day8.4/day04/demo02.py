"""
    for
        for 变量 in 可迭代对象:
            变量 就是可迭代对象中的每个元素
"""
message = "我爱编程"
# 遍历字符串
for item in message:
    # 打印每个字符
    print(item)

# for item in message:
#     item = "x" # 修改的是变量item存储的地址,没有修改字符串
print(message)
