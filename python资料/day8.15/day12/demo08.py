class Vector2:
    """
        二维向量
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 决定相同的依据
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # 决定大小的依据
    def __lt__(self, other):
        return self.x < other.x


v01 = Vector2(1, 1)
v02 = Vector2(1, 1)
print(v01 == v02)  # True 比较两个对象内容(__eq__决定)
print(v01 is v02)  # False 比较两个对象地址

list01 = [
    Vector2(2, 2),
    Vector2(5, 5),
    Vector2(3, 3),
    Vector2(1, 1),
    Vector2(1, 1),
    Vector2(4, 4),
]
# 必须重写 eq
print(Vector2(5, 5) in list01)
print(list01.count(Vector2(1, 1)))
# 必须重写 lt
list01.sort()
print(list01)