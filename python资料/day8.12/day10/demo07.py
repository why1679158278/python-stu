"""
    属性各种写法

"""
# 写法1：读写属性
# 快捷键：props + 回车
"""
class MyClass:
    def __init__(self,data):
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

m01 = MyClass(10)
print(m01.data)
"""

"""
# 写法2:只读属性
# 适用性：类中确定的数据,类外只能读取,不能修改
# 快捷键：prop + 回车
class MyClass:
    def __init__(self):
        self.__data = 10

    @property
    def data(self):
        return self.__data


m01 = MyClass()
# m01.data = 20# AttributeError: can't set attribute
print(m01.data)
"""

"""
# *写法3：只写属性
class MyClass:
    def __init__(self, data):
        self.data = data

    # data = property()
    
    # @data.setter
    # def data(self, value):
    #     self.__data = value

    def data(self, value):
        self.__data = value

    data = property(fset=data)


m01 = MyClass(10)
print(m01.data)  # AttributeError: unreadable attribute
m01.data = 20
print(m01.__dict__)
"""