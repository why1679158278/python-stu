"""
    时间模块
    https://www.runoob.com/python3/python3-date-time.html
"""

import time

# 1. 时间元组(人类时间)： 公园元年 ～ 现在(2020年8月18日)
time_tuple = time.localtime()
# 年 月 日 时 分 秒 星期(索引) 一年的第几天  夏令时
print(time_tuple)

print(time_tuple[3])  # 获取小时

# 2. 时间戳(计算机时间): 公园1970年元旦现在经过的秒数
print(time.time())  # 1597739927.6006446

# 3. 时间元组 ----> 时间戳
# 时间戳 = time.mktime(时间元组)
print(time.mktime(time_tuple))

# 4. 时间戳 ----> 时间元组
# 时间元组 = time.localtime(时间戳)
print(time.localtime(1597739927.6006446))

# 5. 时间元组  --> 字符串
# 2020/08/18 16:53:46
#  字符串 = time.strftime(格式,时间元组)
print(time.strftime("%Y/%m/%d %H:%M:%S", time_tuple))

# 6.  字符串 -->时间元组
print(time.strptime("2020/08/18 16:53:46", "%Y/%m/%d %H:%M:%S"))
