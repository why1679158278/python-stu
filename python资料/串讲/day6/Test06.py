#字符串中的方法
# 转大写，小写
# str01 = "abcdefg"
# print(str01.upper())
#
# #字符串出现的次数   3  作用   参数：我需要给他什么   返回值： 他会给我什么
# str02 = "从前有个老师叫小帅，小帅很帅，很纯洁，简直就是智慧和勇敢的化身，不信来达内找小帅"
# targetWord = "小帅"
# count = str02.count(targetWord)
# print(count)
# 练习1：从日期字符串（"2008-08-08"）中分析出年、月、日；2008年08月08日。
# 让用户输入一个日期格式如:2008-01-02,你输出你输入的日期为2008年1月2日
# str03 = input("请输入年月日")
# list01 = str03.split("-")
# print("%s年%s月%s日"%(list01[0],list01[1],list01[2]))

#替换 注意：会创建一个字符串的副本
# str04 = "村里的关键人物西西"
# if str04.find("西西") !=-1:
#     str04 = str04.replace("西西","东东")
# print(str04)
#
# str05 = "今天天气好晴朗，处处好风光"
# str05 = str05.lstrip("今")
# print(str05)


# 4. 定义函数，返回字符串中第一个不重复的字符。
# 输入：ABCACDBEFD
# 输出：E

"""
    定义函数，返回字符串中第一个不重复的字符。
    输入：ABCACDBEFD
    输出：E
"""
#查找第一个不重复的字符
#参数：字符串
#返回值：字符（第一个不重复的）

def first_not_repeating_char(targetStr):
    dict_info = get_repeating_info(targetStr)
    return  get_key_value(dict_info,1)

def get_repeating_info(target):
    #字典  键 ：字符    值 ：次数
    dic01={}
    for char in target:
        #空的添加到字典中
        dic01[char] =  target.count(char)
        # if char not in dic01:
        #     dic01[char] = 1
        # #字典中有该字符 次数+1
        # else:
        #     dic01[char] +=1
    return dic01

def get_key_value(dict_info,value):
    for k,v in dict_info.items():
        if v == value:
            return k

print(first_not_repeating_char("ABCACDBEFD"))






