"""
    str --> list
    将一个字符串拆分为多个。
    列表 = “a-b-c-d”.split(“分隔符”)
"""
result = "a-b-c-d".split("-")
print(result)
# 应用：取出一个字符串表达的多种信息
# "悟空,猪八戒,唐僧"
datas = "悟空,猪八戒,唐僧".split(",")
print(datas)
