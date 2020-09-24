"""
    模块导入
    练习:student_info_manager_system.py
        创建目录student_info_manager_system
        创建模块bll,存储XXController
            业务逻辑层 business  logic  layer
        创建模块usl,存储XXView
            用户显示层 user show layer
        创建模块model,存储XXModel
        创建模块main,存储调用XXView的代码
"""
# 导入方式1：import 模块名
# 使用：模块名.成员
# 原理：创建变量名记录文件地址,
#      使用时通过变量名访问文件中成员
# 备注："我过去"
# 适用性：适合面向过程(全局变量、函数)
# import module01
#
# module01.func01()

# 导入方式2.1：from 文件名 import 成员
# 使用：直接使用成员
# 原理：将模块的成员加入到当前模块作用域中
# 备注："你过来"
# 小心：导入进来的成员命名冲突
# 适用性：适合面向对象(类)

# from module01 import func01
#
# def func01():
#     print("demo01 - func01")
#
# func01() # 调用的是自己的func01


# 导入方式2.2：from 文件名 import *
from module01 import *

func01()
func02()
