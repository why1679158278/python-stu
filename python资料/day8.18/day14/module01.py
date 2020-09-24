
# 定义可导出成员
# 只有from module01 import *有效

__all__ = ["func01"]

def func01():
    print("module01 - func01执行喽")


def func02():
    print("module01 - func02执行喽")