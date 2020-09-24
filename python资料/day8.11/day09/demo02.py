"""
    函数参数
        实际参数:与形参进行对应
            位置实参：按顺序
                序列实参：拆
            关键字实参：按名称
                字典实参：拆
"""
def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)
# TypeError: func01() takes 3 positional arguments but 4 were given
# func01(1, 2, 3, 4)
# TypeError: func01() missing 1 required positional argument: 'p3'
# func01(1, 2)

# 1. 位置实参：根据顺序与形参进行对应
func01(1, 3, 2)
# 2. 关键字实参：根据名称与形参进行对应
func01(p1=1, p2=2, p3=3)
func01(p2=2, p1=1, p3=3)
# 使用容器思想传递参数:统一管理数据
# 3.序列实参：将序列拆分后与形参按顺序对应
list01 = ["a", "b", "c"]
func01(*list01)
# 4.字典实参：将字典拆分后与形参按名称对应
dict01 = {"p3": "c", "p1": "a", "p2": "b"}
func01(**dict01)
