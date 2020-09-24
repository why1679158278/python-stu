# 练习：参照day08_exercise02代码
# 在终端中录入边长打印矩形.
# 如果录入失败，重新录入.


def print_rectangular(length_of_side, fill_character):
    for row in range(length_of_side):
        if row == 0 or row == length_of_side - 1:
            print(fill_character * length_of_side)
        else:
            print(fill_character + " " * (length_of_side - 2) + fill_character)


def get_length_of_side():
    while True:
        try:
            length = int(input("请输入矩形边长："))
            return length
        except Exception:
            print("录入有误")


if __name__ == '__main__':
    number = get_length_of_side()
    print_rectangular(number, "$")
