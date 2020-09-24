"""
    模块相关知识
"""

# 1. 模块变量
# 模块的第一个字符串,自动存储__doc__变量中


print(__doc__)

# print(demo01.__doc__)

# 2. 可以通过__all__限制可导出成员
# from module01 import *
from module01 import func02

func02()

# 3. 搜索顺序
# 导入模块是否成功的唯一标准：
# 导入路径 + 系统路径 = 真实路径
import sys

# 根目录:主模块(第一次运行的文件)的文件夹
print(sys.path)# ["根目录",.....,]
