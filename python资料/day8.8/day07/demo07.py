"""
    列表推导式嵌套
"""
list01 = ["香蕉", "苹果", "哈密瓜"]
list02 = ["牛奶", "咖啡", "可乐", "雪碧"]
# list_result = []
# for r in list01:
#     for c in list02:
#         list_result.append(r+c)
list_result = [r + c for r in list01 for c in list02]
print(list_result)
