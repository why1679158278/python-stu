"""
    元组tuple
        基本操作
"""
# 创建
# -- 元组名 = (元素1, 元素2, 元素3)
tuple01 = (10, 20, 30)
# -- 元组名 = tuple( 可迭代对象 )
list01 = ["a", "b", "c"]
tuple02 = tuple(list01)

# 定位
# -- 读取(索引／切片)
print(tuple01[0])
print(tuple01[:2])

# 遍历
for item in tuple01:
    print(item)

for i in range(len(tuple01) - 1, -1, -1):
    print(tuple01[i])

# 注意1：小括号可以省略
tuple03 = 10, 20, 30
# 注意2：如果元组中只有一个元素,必须有逗号
tuple04 = (10,)
print(type(tuple04))
# 拆包:　多个变量　= 容器
# a,b,c = tuple03
# a,b,c = ["A","B","C"]
a,b,c = "孙悟空"
print(a)孙
print(b)悟
print(c)空

*a,b = tuple03
print(a)孙悟
print(b)空