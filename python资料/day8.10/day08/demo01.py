"""
    函数
"""

# 代码的重复是万恶之源
"""
# 当做法改变时,代码需要修改多次
# 做法　+ 使用
print("直拳")
print("摆拳")
print("勾拳")
print("正蹬")

# .....

# 做法　+ 使用
print("直拳")
print("摆拳")
print("勾拳")
print("正蹬")
"""


# 当做法改变时,代码只需要修改一次
# 做法
def attack():
    """
        单次攻击
    """
    print("正蹬")
    print("直拳")
    print("摆拳")
    print("勾拳")

# 用法
attack()# 调试时,需要进入函数体按F7
attack()
attack()
