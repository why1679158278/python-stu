def func01(p1, p2):
    # 将右侧列表地址给到左侧变量
    p1 = [100, 200]
    # 2. 修改可变
    # 将右侧列表中元素给到左侧列表元素
    p2[:] = [300, 400]

# 1. 传入可变
a = [10, 20]
b = [30, 40]
func01(a, b)
print(a)  # [10, 20]
print(b)  # [300, 400] 3. 无需通过返回值
