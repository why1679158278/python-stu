"""
    包

项目根目录
包
    模块
        类
            函数
                语句
"""
# 路径：从项目根目录开始

# 方式1:import 路径.模块 as 别名
# 使用：别名.成员
# import package01.package02.m02 as m
#
# m.func01()

# 方式2:from 路径.模块 import 成员
# from package01.package02.m02 import func01
#
# func01()

# 必须在包的__init__.py文件中添加
# 方式3:import 包
# import ....
import package01.package02 as p

p.m02.func01()

# 方式4:from 包 import 包
from package01 import package02

package02.m02.func01()
