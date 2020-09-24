"""
    以容器思想，完成之前的练习。（赠送）
    在终端中获取月份，打印相应的天数.
"""
# month = int(input("请输入月份:"))
# if 1 <= month <= 12:
#     if month == 2:
#         print("29天")
#     # elif month == 4 or month == 6 or month == 9 or month == 11:
#     elif month in (4, 6, 9, 11):
#         print("30天")
#     else:
#         print("31天")
# else:
#     print("月份有误")

month = int(input("请输入月份:"))
# 将每月天数存入容器
days_of_month = (31, 29, 31, 30, 31,
                 30, 31, 31, 30, 31, 30, 31)
print(days_of_month[0])  # 一月
print(days_of_month[2])  # 三月
print(days_of_month[month - 1])






