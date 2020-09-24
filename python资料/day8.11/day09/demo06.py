"""
    函数参数
        形式参数
"""


# 双星号字典形参：关键字实参数量无限   合
def func01(**kwargs):
    print(kwargs)

func01(p1=1, p2=2)# {'p1': 1, 'p2': 2}
