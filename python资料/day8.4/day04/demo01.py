"""
    猜数字2.0
        增加功能:
            最多猜3次,超过次数提示"游戏失败"

    while 条件1:
        ....
        if 条件2:
            break
    else:
        ....
        通过else是否执行,可以判断循环从哪个条件退出的.
"""
import random

random_number = random.randint(1, 100)
print(random_number)

count = 0
while count < 3:
    count += 1
    input_number = int(input("请输入要猜的数字:"))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("恭喜猜对啦,总共猜了" + str(count) + "次")
        break
else:  # 只有从循环条件退出,才执行else.(从break退出不执行else)
    print("游戏失败")
