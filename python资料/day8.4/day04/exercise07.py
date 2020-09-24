"""
    循环录入编码值,打印文字.直到输入空字符串,停止。
"""
while True:
    number = input("请输入数字：")
    if number == "":
        break
    print(chr(int(number)))