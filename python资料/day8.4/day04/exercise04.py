# 练习:使用for循环改写homework/exercise04

# 在终端中累加 0  1  2  3
# 在终端中累加 2  3  4  5  6
# 在终端中累加 1  3  5  7
# 在终端中累加 8  7  6  5  4
# 在终端中累加 -1  -2  -3  -4  -5

result = 0
for number in range(4):
    result += number
print(result)

result = 0
for number in range(2, 7):
    result += number
print(result)

result = 0
for number in range(1, 8, 2):
    result += number
print(result)

result = 0
# 因为倒序,所以不包含3,而包含4
for number in range(8, 3, -1):
    result += number
print(result)

result = 0
# 因为倒序,所以不包含3,而包含4
for number in range(-1, -6, -1):
    result += number
print(result)
