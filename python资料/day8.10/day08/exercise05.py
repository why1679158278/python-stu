# 练习:参照day03/exercise03代码
# 创建函数,根据课程阶段计算课程名称.
# number = input("请输入课程阶段数：")
# if number == "1":
#     print("Python语言核心编程")
# elif number == "2":
#     print("Python高级软件技术")
# elif number == "3":
#     print("Web全栈")
# elif number == "4":
#     print("网络爬虫")
# elif number == "5":
#     print("数据分析、人工智能")

def get_course_name(number):
    """
        获取课程阶段名称
    :param number: str类型,课程编号
    :return: 课程名称
    """
    # dict_course = {
    #     "1": "Python语言核心编程",
    #     "2": "Python高级软件技术",
    #     "3": "Web全栈",
    #     "4": "网络爬虫",
    #     "5": "数据分析、人工智能",
    # }
    # if number in dict_course:
    #     return dict_course[number]

    tuple_course = (
        "Python语言核心编程",
        "Python高级软件技术",
        "Web全栈",
        "网络爬虫",
        "数据分析、人工智能",
    )
    index = int(number) - 1
    if 0 <= index <= len(tuple_course) - 1:
        return tuple_course[index]

result = get_course_name("8")
print(result)
