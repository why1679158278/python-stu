"""
    练习:在终端中,循环录入字符串,如果录入空则停止.
         停止录入后打印所有内容(一个字符串)
"""
list_temps = []
while True:
    content = input("请输入内容：")
    if content == "":
        break
    list_temps.append(content)
result = "".join(list_temps)
print(result)














