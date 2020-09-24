"""
    中国疫情地图
    1. 注释：给人看的,对代码的描述
    2. 导入：from 文件 import 内容
    3. 函数：功能
        写法1：
          制作
                def 函数名():
                    函数体

          使用
                函数名()
        写法2：
          制作
                def 函数名(参数1,参数2):
                    函数体

          使用
                函数名(数据1,数据2)
"""

from pyecharts.charts import Map
from pyecharts.options import *
from dingxiang_spider import data

# 创建地图
map = Map()
# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(max_=1000)
)
# 添加
map.add("中国疫情地图", data)
# 渲染
map.render()
