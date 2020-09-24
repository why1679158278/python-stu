"""
    异常处理
        目标：不是针对代码写错进行处理
             而是针对运行时,数据操作有效范围而引发的错误.
        现象：程序不再向下执行,不断向上返回,直到最初的调用语句.
        作用：将异常状态(不断向上),改为正常状态(向下执行).
        价值：保障程序按照既定流程处理
"""
# 代码写错了：
# print(qtx)# NameError: name 'qtx' is not defined
# print("1" + 1)# TypeError: must be str, not int
# class Wife:
#     pass
# w01 = Wife()
# print(w01.name)# AttributeError: 'Wife' object has no attribute 'name'


# 需要使用异常处理解决的问题：
"""
def div_apple(apple_count):
    # ValueError
    person_count = int(input("请输入人数："))
    # ZeroDivisionError
    result = apple_count / person_count
    print(f"每人{result}个苹果")
    
def main():
    div_apple(10)

main()
"""


# 写法1:"包治百病"
def div_apple(apple_count):
    try:
        # ValueError
        person_count = int(input("请输入人数："))
        # ZeroDivisionError
        result = apple_count / person_count
        print(f"每人{result}个苹果")
    except Exception:
        print("程序出错啦")

# 写法2:"对症下药" (官方推荐)
"""
def div_apple(apple_count):
    try:
        # ValueError
        person_count = int(input("请输入人数："))
        # ZeroDivisionError
        result = apple_count / person_count
        print(f"每人{result}个苹果")
    except ValueError:
        print("输入的不是整数")
    except ZeroDivisionError:
        print("输入的是0")
"""

# 写法3:不管是否错误或哪种错误,一定执行某些逻辑.
"""
def div_apple(apple_count):
    try:
        # 打开文件
        # 处理...
        
        # ValueError
        person_count = int(input("请输入人数："))
        # ZeroDivisionError
        result = apple_count / person_count
        print(f"每人{result}个苹果")
    except ValueError:
        print("输入的不是整数")
    finally:# 无论对错一定执行的代码
        # 关闭文件
        print("游戏结束")
"""

# 写法4:程序没有错误,执行的逻辑.
"""
def div_apple(apple_count):
    try:
        person_count = int(input("请输入人数：")) 
        result = apple_count / person_count
        print(f"每人{result}个苹果")
    except Exception:
        print("程序出错啦")
    else:
        print("游戏胜利")
"""
div_apple(10)

print("后续逻辑")
