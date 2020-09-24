# 练习:在终端中录入任意整数,计算累加和.
# "1234" -> "1" -> 累加 1
number = input("请输入一个整数:")
sum_value = 0
for item in number:
    sum_value += int(item)
print(sum_value)
