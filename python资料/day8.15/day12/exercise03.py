"""
    day10/exercise01
    day10/exercise03
    直接打印商品对象: xx的编号是xx,单价是xx
    直接打印敌人对象: xx的攻击力是xx,血量是xx
    拷贝两个对象,修改拷贝前数据,打印拷贝后数据.
    体会拷贝的价值.
"""


class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __str__(self):
        return "%s的编号是%d,单价是%d" % (self.name, self.cid, self.price)

    def __repr__(self):
        return "Commodity(%d, '%s', %d)" % (self.cid, self.name, self.price)
class Enemy:
    def __init__(self, name="", atk=0, hp=0):
        self.name = name
        self.atk = atk
        self.hp = hp
bxjg = Commodity(1001, "变形金刚", 300)
print(bxjg)

bxjg2 = eval(bxjg.__repr__())
print(bxjg2)
