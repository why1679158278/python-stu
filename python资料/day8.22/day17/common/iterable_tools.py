"""
    可迭代对象 工具

    自定义高阶函数
        1. 教学目的:复习之前的知识点,对内置高阶函数更加了解.
        2. 实用价值：功能无限强大(后续不断增加新功能)
                   跨语言
        3. 增加面试成功率
               精通函数式编程
               源于微软Linq技术
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
    def get_count(iterable, func_condition):
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

    @staticmethod
    def find_single(iterable, func_condtion):
        """
            在可迭代对象中,根据指定条件查找单个元素.
        :param iterable:需要搜索的可迭代对象
        :param func_condtion:函数类型的搜索条件
        :return:满足条件的单个元素
        """
        for item in iterable:
            if func_condtion(item):
                return item

    @staticmethod
    def select(iterable, func_handle):
        """
            在可迭代对象中，根据逻辑查询某些属性.
        :param iterable:可迭代对象
        :param func_handle:查询的逻辑
        :return:生成器,推算某些属性
        """
        for emp in iterable:
            yield func_handle(emp)

    @staticmethod
    def get_max(iterable,func_condition):
        """
            在可迭代对象中，根据传入的条件查找最大的元素
        :param iterable:需要搜索的可迭代镀锡
        :param func_condition:查找最大值条件
        :return:最大的元素
        """
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            if func_condition(max_value) < func_condition(iterable[i]):
                max_value = iterable[i]
        return max_value

    @staticmethod
    def delete_all(iterable, func_condition):
        """

        :param iterable:
        :param func_condition:
        :return:
        """
        count = 0
        for i in range(len(iterable) - 1, -1, -1):
            if func_condition(iterable[i]):
                del iterable[i]
                count += 1
        return count

    @staticmethod
    def order_by(iterable, func):
        """

        :param iterable:
        :param func:
        :return:
        """
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                if func(iterable[r]) > func(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]
