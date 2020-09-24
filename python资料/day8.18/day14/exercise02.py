"""
    day06/exercise06
    定义函数,根据年月日,计算这是这一年的第几天.
"""
import time


def get_total_days(year, month, day):
    """
        获取本年第几天
    :param year:年份
    :param month:月份
    :param day:天
    :return:总天数
    """
    time_tuple = time.strptime(
        f"{year}/{month}/{day}", "%Y/%m/%d")

    return time_tuple[-2]

print(get_total_days(2020, 8, 18))

