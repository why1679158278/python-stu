"""
    在终端中循环录入5个成绩,
    最后打印平均成绩(总成绩除以人数)
"""

sum_score = 0
count = 0
while count < 5:
    score = int(input("请输入成绩"))
    sum_score += score
    count += 1

print(sum_score / 5)
