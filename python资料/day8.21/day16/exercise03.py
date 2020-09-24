# 练习1:在列表中获取所有整数,并计算它的平方.
# 要求：使用列表推导式，生成器表达式完成.
# 通过调试，体会差异.

list01 = [43, "a", 5, True, 6, 7, 89, 9]

list_result01 = [item ** 2 for item in list01 if type(item) == int]
for item in list_result01:
    print(item)

generator_result02 = (item ** 2 for item in list01 if type(item) == int)
for item in generator_result02:
    print(item)

# 练习2:在列表中获取所有大于10的小数.
list02 = [43.6, 54.1, 5.7, 65.3, 67.5, 8.7]
list_result02 = [item for item in list02 if item > 10]
for item in list_result02:
    print(item)

generator_result02 = (item for item in list02 if item > 10)
for item in generator_result02:
    print(item)

