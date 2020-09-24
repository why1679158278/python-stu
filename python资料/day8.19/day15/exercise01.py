# 练习：调用获取成绩函数,一定能够得到成绩
# 如果录入错误,重新录入(循环while).

# def get_score():
#     try:
#         score = float(input("请输入成绩："))
#         return score  # 如果异常,不会执行到本行
#     except Exception:
#         print("录入有误")  # 异常被处理完毕


def get_score():
    while True:
        try:
            score = float(input("请输入成绩："))
            return score  # 如果异常,不会执行到本行
        except Exception:
            print("录入有误")  # 异常被处理完毕


print(get_score())
