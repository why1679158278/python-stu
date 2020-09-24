"""
    创建图形管理器
	1. 记录多种图形（圆形、矩形....）
	2. 提供计算总面积的方法.
    满足：
        开闭原则
    测试：
        创建图形管理器，存储多个图形对象。
        通过图形管理器，调用计算总面积方法.

    三大特征：
        封装：GraphicManager、Rectangle、Cycle
        继承：Graphic隔离了Rectangle、Cycle
        多态：以重写的方式完成具体图形算法
    六大原则：
        开闭原则：增加新图形，不改变图形管理器
        单一职责：
        依赖倒置：GraphicManager用Graphic，不用Rectangle、Cycle
        组合复用：GraphicManager通过实例变量调用图形算法
"""


class GraphicManager:
    def __init__(self):
        self.__list_graphics = []

    def add_graphic(self, graphic):
        self.__list_graphics.append(graphic)

    def calcualte_total_area(self):
        total_area = 0
        for graphic in self.__list_graphics:
            total_area += graphic.get_total_area()
        return total_area


class Graphic:
    def get_total_area(self):
        pass

# ---------------------------
class Rectangle(Graphic):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def get_total_area(self):
        super().get_total_area()
        return self.l * self.w


class Circle(Graphic):
    def __init__(self, r):
        self.r = r

    def get_total_area(self):
        return 3.14 * self.r ** 2


manager = GraphicManager()
manager.add_graphic(Rectangle(2, 4))
manager.add_graphic(Circle(5))
print(manager.calcualte_total_area())
