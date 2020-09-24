"""
    MyRange1.0版本
        提示：创建类
             创建构造函数
             创建__iter__
             ...
"""


class MyRangeIterator:
    def __init__(self, stop):
        self.__number = -1
        self.__stop = stop

    def __next__(self):
        if self.__number == self.__stop - 1:
            raise StopIteration()
        self.__number += 1
        return self.__number


class MyRange:
    def __init__(self, end):
        self.__end = end

    def __iter__(self):
        return MyRangeIterator(self.__end)


# for number in MyRange(5):
#     print(number)# 0 1 2 3 4

my_range = MyRange(5)
iterator = my_range.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
