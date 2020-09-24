"""
    参照day04/exercise09代码
    创建函数,在终端中打印矩形.
"""


# number = int(input("请输入整数:"))  # 5
# for row in range(number):
#     if row == 0 or row == number - 1:
#         print("*" * number)
#     else:
#         print("*%s*" % (" " * (number - 2)))

def print_rectangular(length_of_side, fill_character):
    """
        在终端中打印空心矩形
    :param length_of_side:边长
    :param fill_character:填充字符　
    """
    for row in range(length_of_side):
        if row == 0 or row == length_of_side - 1:
            print(fill_character * length_of_side)
        else:
            print(fill_character + " " * (length_of_side - 2) + fill_character)


print_rectangular(5, "*")
number = int(input("请输入整数："))
print_rectangular(number, "$")
