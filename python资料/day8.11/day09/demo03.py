"""
    函数参数
        形式参数
            默认形参
            位置形参
"""
# 1. 默认形参:允许实参不传递
# 注意：必须从右向左依次存在
def func01(p1="", p2=0.5, p3=0):
    print(p1)
    print(p2)
    print(p3)

func01(p3=2)  # 关键字实参
func01("a")  # 位置实参
func01("a", p3=3)  # 关键字实参 + 位置实参


# 2. 位置形参:实参必须传递
def func02(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)
