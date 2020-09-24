"""
    bool 类型操作(1)
        int类型　   ... -1　0 1  10 ...
        bool类型   真True  假False
            命题：带有判断性质的陈述句
        比较运算符：
            等于 ==   不等于!=
            >  <   >=   <=
    练习:exercise09
"""
# 命题：我是一个总统
# 假的
# result = input("输入请您的职业:") == "总统"
# print(result) # False

result = 10 <= int(input("请输入年龄:")) <= 30
print(result)