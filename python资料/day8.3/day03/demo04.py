"""
    if 真值表达式
        if 值:  # 自动转换为 bool(值)
            .....
    练习:exercise07
"""
# 转换结果为false的值:0   0.0   ""  None ....
# 核心逻辑:有值,则为True
print(bool(0))

if 100:  # bool(100)
    print("真值")

# 应用
content = input("请输入内容:")
# if content != "": # 输入的不是空字符串
if content: # 有值
    print("您输入的是:" + content)
else:
    print("您没输入内容")
