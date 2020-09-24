region = "湖北"
confirmed = 67802
cure = 63326
rate_cure = 0.99
print("%s确诊%d人,治愈%d人,治愈率%.1f" % (region, confirmed, cure, rate_cure))
print(f"{region}确诊{confirmed}人,治愈{cure}人,治愈率{rate_cure:.1f}")

total_second = 70
minute = total_second // 60
second = total_second % 60
print("%d秒是%.2d分零%d秒" % (total_second, minute, second))
print(f"{total_second}秒是{minute:02}分零{second}秒")
