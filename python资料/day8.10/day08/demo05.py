# -------创建函数-------
def attack():
    print("正蹬")
    print("直拳")
    print("摆拳")
    print("勾拳")


def repeated_attack(count):
    for __ in range(count):
        attack()


# -------使用函数-------
repeated_attack(3)
