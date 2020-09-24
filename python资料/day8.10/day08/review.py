"""
    复习
"""
# 1. 创建
list_numbers = [10,20,30]
# 2. 添加
list_numbers.append(40)
list_numbers.insert(1,40)
# 3. 定位
print(list_numbers[-1])# 查找最后一个元素
list_numbers[0] = 100

# 通过切片读取数据：浅拷贝
print(list_numbers[: 2])
#　通过切片修改数据：遍历右侧,依次存入
list_numbers[-2:] = "悟空"
print(list_numbers)
# 右侧５个数据   左侧2个数据
# list_numbers[-2:] = ["a","b","c","d","e"]
# 右侧５个数据   左侧0个数据（插入）
# list_numbers[1:1] = ["a","b","c","d","e"]
# 右侧0个数据   左侧3个数据（删除）
# list_numbers[1:-1] = []
# 4. 遍历
# 从头到尾依次读取
for number in list_numbers:
    print(number)

for i in range( len(list_numbers)-1 , -1 , -1  ):
    print(list_numbers[i])

# 5. 删除
list_numbers.remove(10)
del list_numbers[0]
del list_numbers[:2]