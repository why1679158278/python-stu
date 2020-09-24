"""
    参照day03/exercise05代码
    创建函数,计算IQ等级
"""


# ma = int(input("请输入你的心里年龄："))
# ca = int(input("请输入你的实际年龄："))
# iq = ma / ca * 100
#
# if 140 <= iq:
#     print("天才")
# elif 120 <= iq:
#     print("超常")
# elif 110 <= iq:
#     print("聪慧")
# elif 90 <= iq:
#     print("正常")
# elif 80 <= iq:
#     print("迟钝")
# else:
#     print("低能")

# def get_IQ_level(ma, ca):
#     iq = ma / ca * 100
#     if 140 <= iq:
#         return "天才"
#     elif 120 <= iq:# 如果上一个条件满足,return后退出函数,当天条件不会判断
#         return "超常"
#     elif 110 <= iq:
#         return "聪慧"
#     elif 90 <= iq:
#         return "正常"
#     elif 80 <= iq:
#         return "迟钝"
#     else:
#         return "低能"

def get_IQ_level(ma, ca):
    iq = ma / ca * 100
    if 140 <= iq:
        return "天才"
    if 120 <= iq:
        return "超常"
    if 110 <= iq:
        return "聪慧"
    if 90 <= iq:
        return "正常"
    if 80 <= iq:
        return "迟钝"
    return "低能"


level = get_IQ_level(30, 25)
print(level)
