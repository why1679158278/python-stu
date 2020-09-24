"""
    根据exercise02三个列表
        -- 打印新疆疫情信息(xx地区新增xx人现存xx人)
        -- 将地区列表list_region修改为
            ["HK","XJ","LN"]
        -- 打印地区列表元素(一行一个)
        -- 倒序打印新增列表元素(一行一个)
"""
list_region = ["香港", "新疆", "辽宁"]
list_new = [80, 22, 0]
list_now = [1486, 618, 93]

print("%s地区新增%d人现存%d人" % (list_region[1], list_new[1], list_now[1]))
print(f"{list_region[1]}地区新增{list_new[1]}人现存{list_now[1]}人")

list_region[:] = ["HK", "XJ", "LN"]
print(list_region)

for region in list_region:
    print(region)

for i in range(len(list_new) - 1, -1, -1):
    print(list_new[i])
