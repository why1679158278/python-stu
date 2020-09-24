"""
    根据月日,计算是这一年的第几天.
    公式：前几个月总天数 + 当月天数
    例如：5月10日
    计算：31  29  31  30 + 10
"""
month = int(input("请输入月:"))
day = int(input("请输入日:"))
days_of_month = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

# print(days_of_month[0])
# print(days_of_month[1])
# print(days_of_month[2])
# print(days_of_month[3])

# total_days = 0
# for i in range(month - 1):
#     total_days += days_of_month[i]
# total_days += day
# print(total_days)

total_days = sum(days_of_month[:month - 1])
total_days += day
print("%d月%d日是第%d天." % (month, day, total_days))
print(f"{month}月{day}日是第{total_days}天.")
