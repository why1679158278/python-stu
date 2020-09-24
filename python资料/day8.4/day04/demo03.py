"""
    for + range
    range 范围
        产生一个范围的整数
"""
# 写法1: range(开始,结束,间隔)
# 注意:不包含结束值
# for number in range(1,11,2):
#     print(number)# 1 3 5 7 9

# 写法2: range(开始,结束)
# 注意:间隔默认为1
# for number in range(1,5):# 1 2 3 4
#     print(number)

# 写法3: range(结束)
# 注意:开始默认为1
for number in range(5):#0 1 2 3 4
    print(number)
