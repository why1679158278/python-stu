"""
    在exercise02基础上,增加参数和返回值。
    修改装饰器
"""


def verify_permissions(func):
    def wrapper(*args, **kwargs):
        print("验证权限")
        return func(*args, **kwargs)  # 执行旧功能

    return wrapper  # 返回内函数


@verify_permissions
def insert(data):
    print("插入", data)
    return 1002


@verify_permissions
def delete(id):
    print("删除", id)
    return "ok"


print(insert("数据"))  # 1002
print(delete(1001))  # ok
