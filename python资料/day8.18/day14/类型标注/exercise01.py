"""
    创建图形管理器
        1. 记录多种图形（圆形、矩形....）
        2. 提供计算总面积的方法.
    满足：
        开闭原则、依赖倒置
    测试：
        创建图形管理器，存储多个图形对象。
        通过图形管理器，调用计算总面积方法.
"""


class Graphic:
    def get_area(self):
        pass

class GraphicManager:
    def __init__(self):
        self.list_graphics = []

    def add_graphic(self, graphic:Graphic):
        # 1. 编码时 调用 父
        # 2. 运行时 执行 子
        self.list_graphics.append(graphic)

    def calculate_total_area(self):
        total_area = 0
        for item in self.list_graphics:
            total_area += item.get_area()
        return total_area

# -------------------

class Circle(Graphic):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return 3.14 * self.r


class Rectanle(Graphic):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def get_area(self):
        return self.l * self.w


if __name__ == '__main__':
    manager = GraphicManager()
    manager.add_graphic(Circle(5))
    manager.add_graphic(Rectanle(5, 6))
    manager.add_graphic(Rectanle(5, 6))
    print(manager.calculate_total_area())
