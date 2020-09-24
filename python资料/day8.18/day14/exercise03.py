# 练习：定义函数,根据年月日,计算星期。
#       星期一  星期二  .....  星期日
import time

def get_week(year, month, day):
    """
        获取本年第几天
    :param year:年份
    :param month:月份
    :param day:天
    :return:总天数
    """
    time_tuple = time.strptime(
        f"{year}/{month}/{day}", "%Y/%m/%d")

    week_index = time_tuple[-3]
    tuple_weeks = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
    return tuple_weeks[week_index]


print(get_week(2020, 8, 18))
