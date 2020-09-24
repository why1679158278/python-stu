"""
    函数参数
        形式参数
"""
# 命名关键字形参p1 p2：要求必须是关键字实参
# 星号以后的位置形参
def func01(*args, p1, p2):
    print(args)
    print(p1)
    print(p2)
# func01(1, 2, 3, 4, 5)
func01(1, 2, 3, p1=4, p2=5)
func01(p1=4, p2=5)


def func02(*, p1, p2):
    print(p1)
    print(p2)


func02(p1=4, p2=5)

# print(需要打印的信息,sep = 连接符,end=结束符)
print(1, 2, 3, 4, 5, sep="-", end=" ")
# print(1, 2, 3, 4, 5, "-", " ")
print(6, 7, 8)

# 在终端中打印：
# 悟空_八戒_唐僧
# 沙僧-小白龙
print("悟空", "八戒", "唐僧", sep="_")
print("沙僧", "小白龙", "唐僧", sep="-")
