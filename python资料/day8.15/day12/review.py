"""
    封装
        封装数据：多个 包装成  一个
                XXXModel
        封装行为：隐藏
                __名称
        设计思想：
            分而治之、变则疏之
            M    V    C
               显示 与 控制  分离
"""
class XXView:
    def __init__(self):
        self.controller = XXController()

    def func01(self):
        self.controller.func02()

class XXController:
    def func02(self):
        pass

view = XXView()
view.func01()