"""
    内置可重写函数
        __repr__

    总结：
        对象转换为字符串可以重写__str__或者__repr__
        如果为了展示(给人看)选择__str__
        如果为了拷贝(eval)选择__repr__
"""

class Person(object):
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    # 对象 -> 字符串:给解释器看的(必须满足Python语法)
    def __repr__(self):
        return "Person('%s',%d)"%(self.name,self.age)

wk = Person("悟空",25)
message = wk.__repr__()# "Person("悟空",25)"
# 拷贝自定义对象
# eval 将字符串作为python代码执行
wk2 = eval(   message   ) # 创建新悟空对象
print(wk2.name)

