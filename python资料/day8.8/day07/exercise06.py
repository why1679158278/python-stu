"""
    多个人的多个爱好
    1. 打印于谦的所有爱好(一行一个)
    2. 计算郭德纲所有爱好数量
    3. 打印所有人(一行一个)
    4. 打印所有爱好(一行一个)
"""
dict_hobbies = {
    "于谦": ["抽烟", "喝酒", "烫头"],
    "郭德纲": ["说", "学", "逗", "唱"],
}
for item in dict_hobbies["于谦"]:
    print(item)

print(len(dict_hobbies["郭德纲"]))

for key in dict_hobbies:
    print(key)

for value in dict_hobbies.values():
    for item in value:
        print(item)