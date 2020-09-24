"""
    玩家攻击敌人,敌人受伤(头顶爆字).
"""


class Player:
    def attack(self, target):
        # 谁.受伤()
        target.damage()


class Enemy:
    def damage(self):
        print("头顶爆字")


player = Player()
enemy = Enemy()
player.attack(enemy)
