"""
    情景：手雷爆炸，可能伤害敌人(头顶爆字)或者玩家(碎屏)。
    变化：还可能伤害房子、树、鸭子....
    要求：增加新事物，不影响手雷.
    画出架构设计图
    体会：开闭原则
        增加新攻击目标,手雷不改变.

    封装：

    继承：

    多态：
"""
# --------------架构师----------------

class Grenade:
    def explode(self,target):
        print("手雷爆炸")
        target.damage()

class AttackTarget:
    def damage(self):
        pass

# --------------程序猿----------------

class Enemy(AttackTarget):

    def damage(self):
        print("头顶爆字")

class Player(AttackTarget):

    def damage(self):
        print("碎屏")

# --------------测试----------------
g = Grenade()
g.explode(    Enemy()   )
g.explode(    Player()   )