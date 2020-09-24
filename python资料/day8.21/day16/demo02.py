"""
    内置生成器
        zip
"""
list01 = ["张无忌", "赵敏", "周芷若"]
list02 = [1001, 1002]
for item in zip(list01, list02):
    print(item)
