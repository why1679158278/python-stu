"""
6. 一个小球从100m高度落下,每次弹回原高度一半.
   计算:
    -- 总共弹起多少次?(最小弹起高度0.01m)   13 次
    -- 全过程总共移动多少米?
"""
height = 100
count = 0
distance = height
# 判断弹之前的高度
# while height > 0.01:
# 判断弹之后的高度
while height / 2 >0.01:
    # 弹起来
    height /= 2
    count += 1
    distance += height *2 # 累加起落
    print(f"第{count}次弹起来的高度是{height}")

# print("总共弹起%d次" % count)
print(f"总共弹起{count}次")
print("全过程总共移动%.2f米" % distance)
