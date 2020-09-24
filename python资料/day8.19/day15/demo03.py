"""
    迭代Iteration
        一次重复的结果,将作为下一次重复的开始.
    迭代器iterator
        具有__next__方法的对象
        能够获取下一个数据
    可迭代对象iterable
        具有__iter__方法的对象
        能够获取迭代器的对象
"""
message = "我是齐天大圣孙悟空"
# for item in message:
#     print(item)



# for循环原理
# 1. 获取迭代器对象
iterator = message.__iter__()
while True:
    try:
        # 2. 获取下一个数据
        item = iterator.__next__()
        print(item)
    # 3. 如果遇到异常,则停止循环
    except StopIteration:
        break




# 对象能够被for的条件是什么?
# 答：对象具有__iter__方法
# 答：对象可以获取迭代器

