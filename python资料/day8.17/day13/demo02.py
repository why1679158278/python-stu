"""
    老张开车去东北
    变化：如果增加了飞机、轮船、自行车....等交通工具

        封装：分
            创建人类与汽车类
                去   形势
                  调用
        继承：隔

        多态：做
"""

class Person():
    def go_to(self, vehicle):
        # 先确定的用法
        # 调用的是父类(交通工具)
        # 执行的是子类(汽车)
        vehicle.transport()

class Vehicle:
    """
        抽象(具体的交通工具)
        统一
        隔离
    """
    def transport(self):
        pass

class Car(Vehicle):
    def transport(self):
        print("嘟嘟嘟")

class Airplane(Vehicle):
    def transport(self):
        print("嗖嗖嗖~")

lz = Person()
lz.go_to( Car() )