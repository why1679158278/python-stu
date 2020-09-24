import copy
list01 = ["北京",["上海","深圳"]]
list02 = list01
list03 = list01[:]
list04 = copy.deepcopy(list01)
list04[0] = "北京04"
list04[1][1] = "深圳04"
print(list01) # 修改深拷贝后的数据,不影响拷贝前
list03[0] = "北京03"# 修改第一层,不影响拷贝前
list03[1][1] = "深圳03"# 修改第二层,影响拷贝前
print(list01) # ?
list02[0] = "北京02"# 等同于修改list01
list02[1][1] = "深圳02"
print(list02) # ?
