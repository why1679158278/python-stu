"""
    Python语言的设计理念：
        代码简洁自由,开发效率高.
        其他语言：
            int number = 100;
            number = "007";  x 错误
        python:
            number = 100
            number = "007"
        类型标注：
            number:int = 100
            当变量有了类型，就意味着变量有了对应的操作提示
    缺点：
        不利于开发大型项目。
        制作
            def 函数名(参数名称):
                ...
        使用
            函数名(?)

    Typing 类型标注：
        python3.5 新功能,可以为变量增加类型标注(标记注释).
        作用：
            易于理解
            类型检查
            方便开发
        语法：
            变量名:类型
            -> 返回值类型
            # type:类型
        typing：
            List[类型] 标注列表元素的类型
            Union[类型1,类型2] 标注可以选择的多种类型
            Optional[类型1,类型2] 相当于Union[类型1,类型2,None]
"""
from typing import List, Union, Optional


class EpidemicInformationModel: # 套餐
    """
        疫情信息模型
    """

    def __init__(self, region, confirmed, cure, dead=0):
        """
            创建疫情信息对象
        :param region:地区
        :param confirmed:确诊人数
        :param cure:治愈人数
        :param dead:死亡人数
        """
        self.region = region  # type:str
        self.confirmed = confirmed  # type:int
        self.cure = cure  # 饮料
        self.dead = dead  # 冰激凌


class EpidemicInformationManager: # 麦当劳
    """
        疫情信息管理器
    """

    def __init__(self):
        self.__list_epidemics = [] # type:List[EpidemicInformationModel]

    def add_epidemic_info(self, info:EpidemicInformationModel):
        self.__list_epidemics.append(info)

    # def get_epidemic_by_region(self, region) ->Union[EpidemicInformationModel,None]:
    def get_epidemic_by_region(self, region) ->Optional[EpidemicInformationModel]:
        """
            根据地区获取疫情信息
        :param region:地区
        :return:疫情信息对象
        """
        for item in self.__list_epidemics:
            if item.region == region:
                return item


if __name__ == '__main__':
    manager = EpidemicInformationManager()
    # manager.add_epidemic_info("湖北")
    manager.add_epidemic_info(EpidemicInformationModel("湖北", 66337, 28993))
    # manager.add_epidemic_info(EpidemicInformationModel("四川", 538, 351, 3))
    epidemic = manager.get_epidemic_by_region("四川")
    print(epidemic.region, epidemic.confirmed, epidemic.cure, epidemic.dead)
