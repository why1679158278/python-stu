"""
    运算符重载
        数学运算符
"""


class Vector2:
    """
        二维向量
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x是:%d,y是:%d" % (self.x, self.y)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

v01 = Vector2(1, 2)
v02 = Vector2(2, 3)
print(v01 + v02)  # v01.__add__(v02)
