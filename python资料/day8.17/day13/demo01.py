"""
    老张开车去东北
    变化：如果增加了飞机、轮船、自行车....等交通工具

        封装
            创建人类与汽车类
                去   形势
                  调用
        继承
        多态
"""
# 开闭原则
# 允许 增加新功能  不允许 修改客户端的代码

class Person:
    def go_to(self, vehicle):
        if type(vehicle) == Car:
            vehicle.run()
        elif type(vehicle) == Airplane:
            vehicle.fly()

class Car:
    def run(self):
        print("嘟嘟嘟~")

class Airplane:
    def fly(self):
        print("嗖嗖嗖~")


zl = Person()
bm = Car()
a = Airplane()
zl.go_to(bm)
