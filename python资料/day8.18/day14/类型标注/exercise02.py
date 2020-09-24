import time

tuple_time = (2020, 7, 21, 19, 0, 0, 0, 0, 0)
tuple_time = time.localtime()
print(time.strftime("%Y-%m-%d", tuple_time))
