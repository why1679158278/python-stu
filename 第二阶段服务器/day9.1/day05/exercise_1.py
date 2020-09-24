"""
通过编程完成
 使用input 输入一个端口的名字
 获取这个端口对应的 address is 的值

 提示： 段之间有空行
       每段的第一个单词是端口名称

 思路： 1.先确定是哪一段
       2.从这段中匹配内容
"""
import re

# 拆分段落，提供每一段的内容 生成器
def get_info():
    file = open('log.txt')
    while True:
        data = ""
        for line in file:
            # 遇到空行则表示一段结束
            if line == '\n':
                break
            data += line

        if not data:
            # 到文件结尾则结束
            file.close()
            return
        else:
            yield data # 提供每段内容

def get_address(port):
    # 通过生成器获取每一段
    for info in get_info():
        obj = re.match("\S+",info) # 匹配不到NOne
        if obj.group() == port:
            pattarn = "([0-9a-f]{4}\.){2}[0-9a-f]{4}"
            # 匹配地址
            result = re.search(pattarn,info)
            if result:
                return result.group()
            else:
                return "Unknown"


if __name__ == '__main__':
    port = input(">>")
    print(get_address(port))
