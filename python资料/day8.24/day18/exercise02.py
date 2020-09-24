"""
    在不改变插入与删除定义与调用的情况下，
    为其增加验证权限的新功能
"""

def verify_permissions(func):  # 2
    def wrapper():  # 4
        print("验证权限")  # 新功能
        func()  # 旧功能

    return wrapper

@verify_permissions  # 1
def insert():  # 5
    print("插入")


@verify_permissions
def delete():
    print("删除")


# insert = verify_permissions(insert)

insert()  # 3
delete()
