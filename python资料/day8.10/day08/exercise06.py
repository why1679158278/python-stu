"""
    参照day03/homework/exercise03代码
    创建函数,计算梯形面积.
"""

def get_trapezoidal_area(top_base, bottom_base, height):
    result = (top_base + bottom_base) * height / 2
    return result

area = get_trapezoidal_area(2, 5, 3)
print(area)
