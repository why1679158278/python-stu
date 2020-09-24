"""
    可迭代对象 工具
"""


class IterableHelper:
    """
        可迭代对象助手类
    """

    # 静态方法：不需要操作实例成员与类成员
    @staticmethod
    def find_all(iterable, func_condtion):
        """
            在可迭代对象中,根据指定条件查找所有元素.
        :param iterable:需要搜索的可迭代对象
        :param func_condtion:函数类型的搜索条件
        :return:生成器,用于推算满足条件的元素
        """
        for item in iterable:
            if func_condtion(item):
                yield item

    @staticmethod
    def get_count(iterable,func_condition):
        """
            在可迭代对象中,获取满足条件的元素数量.
        :param iterable:需要搜索的可迭代对象
        :param func_condition:函数类型,搜索条件
        :return:int类型,满足条件的元素数量
        """
        count = 0
        for emp in iterable:
            if func_condition(emp):
                count += 1
        return count
