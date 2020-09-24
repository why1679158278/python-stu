from usl import StudentView

# 模块名
# 如果当前模块是主模块(第一次运行的模块)，那么变量存储的一定是__main__
# 否则是真实模块名
# print(__name__)

# 快捷键：main + 回车
# 如果当前模块是主模块,才执行if内部代码
if __name__ == '__main__':
    view = StudentView()
    view.main()