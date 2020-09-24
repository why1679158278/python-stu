# 练习：定义数值累乘的函数
def multiplicative(*args):
    result = 1
    for number in args:
        result *= number
    return result

print(multiplicative(3,432,342,45,54,56))
print(multiplicative(3,432,342))