print("*", end=" ")
print("*", end=" ")
print("*", end=" ")
print("*", end=" ")
print()# 换行

print("*", end=" ")
print("*", end=" ")
print("*", end=" ")
print("*", end=" ")
print("*", end=" ")
print()# 换行
"""

# 外层循环执行一次
# 内层循环执行多次
for r in range(3):  # 0      1     2
    for c in range(4):  # 0123   0123   0123
        print("*", end=" ")
    print()  # 换行
