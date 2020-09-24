"""
    多继承
        如果父级具有同名方法,会在按照mro顺序调用.
        如果希望调用某个方法,通过类名.方法名(对象)

        继承不要作为代码的复用方式
        继承就是在隔离变化(多继承在隔离多种变化)

        继承：隔离变化
        组合：连接变化
"""


class A:
    def func01(self):
        print("A")


class B(A):
    def func01(self):
        print("B")


class C(A):
    def func01(self):
        print("C")


class D(C, B):
    def func01(self):
        print("D")
        # super().func01()
        A.func01(self)


d = D()
d.func01()
# 查看某个类型的同名方法解析顺序
print(D.mro())
