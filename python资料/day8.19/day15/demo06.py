"""
    MyRange2.0版本 yield
"""
class MyRange:
    def __init__(self, end):
        self.__end = end

    def __iter__(self):
        number = 0
        while number <  self.__end:
            yield number
            number += 1

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
