list01 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]

# 1. 将第一行从左到右逐行打印
for item in list01[0]:
    print(item)
# 2. 将第二行从右到左逐行打印
for c in range(len(list01[1]) - 1, -1, -1):
    print(list01[1][c])
# 3. 将第三列行从上到下逐个打印
# list01[0][2]
# list01[1][2]
# list01[2][2]
for r in range(len(list01)):  # 0 1 2
    print(list01[r][2])
# 4. 将第四列行从下到上逐个打印
# list01[2][3]
# list01[1][3]
# list01[0][3]
for r in range(len(list01) - 1, -1, -1):
    print(list01[r][3])
# 5. 将二维列表以表格状打印
for line in list01:
    for item in line:
        print(item,end = "\t")
    print()