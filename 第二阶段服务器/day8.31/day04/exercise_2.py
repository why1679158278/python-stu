"""
练习： 编写一个程序，将指定目录input下的
大小不到 1024 字节的普通文件文件删除
"""

import os

dir = input(">>") # 输入一个要操作的文件夹

# 获取文件名
for file in os.listdir(dir):
    filename = dir + "/" + file # 文件位置
    # 判断文件大小然后 < 1024则删除之
    if os.path.isfile(filename) and os.path.getsize(filename) < 1024:
        os.remove(filename)