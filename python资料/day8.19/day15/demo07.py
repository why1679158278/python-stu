"""
    MyRange3.0版本 yield -> 生成器
"""
"""
class Generator:# 生成器 = 可迭代对象 + 迭代器
    def __iter__(self):# 可迭代对象
        return self
    
    def __next__(self):# 迭代器
        .....
"""


def my_range(end):
    number = 0
    while number < end:
        yield number
        number += 1


for number in my_range(5):
    print(number)  # 0 1 2 3 4

generator = my_range(5)  # 创建生成器对象
iterator = generator.__iter__()  # 调用生成器的__iter__函数
while True:
    try:
        item = iterator.__next__()  # 通过生成器获取数据
        print(item)
    except StopIteration:
        break
