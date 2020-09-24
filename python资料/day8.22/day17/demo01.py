"""
    lambda 表达式
        匿名函数
            语法：
                lambda 参数:函数体

        传统函数可以，但是lambda不支持：
            lambda 不支持赋值语句
            lambda函数体只支持一条语句
"""

# 1. 有参数 有返回值
# def func01(a, b)
#     return a > b
#
# print(func01(1, 2))

func01 = lambda a, b: a > b

print(func01(1, 2))

# 2. 有参数 无返回值
# def func02(a):
#     print("传入的是：",a)
#
#
# func02(100)

func02 = lambda a: print("传入的是：", a)

func02(100)

# 3. 无参数 有返回值
# def func03():
#     return "这是结果"
#
# print(func03())


func03 = lambda: "这是结果"
print(func03())

# 4. 无参数 无返回值
# def func04():
#     print("func04执行喽")
#
# func04()

func04 = lambda: print("func04执行喽")
func04()


# 5. lambda 不支持赋值语句
# def func05(list_target):
#     list_target[0] = 200
#
#
# list01 = [100]
# func05(list01)
# print(list01)# ???

# lambda list_target:list_target[0] = 200

# 6. lambda函数体只支持一条语句
# def func06():
#     for number in range(5):
#
#
# func06()

# lambda : for number in range(5):print(number)
