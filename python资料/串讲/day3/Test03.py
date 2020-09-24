"""
    列表 list
"""
# 1. 创建列表
# list01 = []
# # 2. 添加
# list01 = [100,"xixi","热"]
# # -- 追加
# list01.append("张三")
# list01.insert(2,"李四")#插的位置 数据
# # 3. 获取
# # 索引：单个
# print(list01[2])
# # 切片：多个
# print(list01[:4])# 创建新列表
#
# # 循环：所有
# for i in list01:
#     print(i)
# # for x in list01[::-1]:
# #     print(x)
# # 倒序
# for i in range(len(list01)-1,-1,-1):
#     print(list01[i])
# 深拷贝 浅拷贝     3
"""
数据的复制： 直接赋值     浅拷贝    深拷贝
 不可变对象： 数字   字符串
 可变对象 ：列表
"""
#引用直接赋值
# a= "xixi"
# print(id(a))
# b = "老王"
# print(id(b))
# b = "张三王二麻子"
# a = b
# print(id(a))
# print(id(b))
# print(a)
# print(b)
#引用直接赋值
# l1 = [1,2,3]
# l2 =l1
# print(id(l1))
# print(id(l2))
# l1[0] = 18
# print(id(l1))
# print(id(l2))
# print(l1)
# print(l2)
#浅拷贝 不可变对象的浅拷贝
#import copy
# a = 10
# b = copy.copy(a)
# print(id(a))
# print(id(b))
import copy
# 浅拷贝
# l1 =[1,2,3]
# l2 = copy.copy(l1)
# print(id(l1))
# print(id(l2))
# l1[0]  = 99
# print(id(l1))
# print(id(l2))
# print(l1)
# print(l2)

# a= [1,2]
# l1 = [3,4,5,a]#34512
# l2 = copy.copy(l1)#34512
# print(id(l1))
# print(id(l2))
# a[0] = 66
# print(id(l1))
# print(id(l2))
# print(l1)#[3, 4, 5, [66, 2]]
# print(l2)#[3, 4, 5, [66, 2]]

# 深度拷贝
# # a= [1,2]
# # l1 = [3,4,5,a]#34512
# # l2 = copy.deepcopy(l1)#34512
# # print(id(l1))
# # print(id(l2))
# # a[0] = 66
# print(id(l1))
# print(id(l2))
# print(l1)#[3, 4, 5, [66, 2]]
# print(l2)#[3, 4, 5, [1, 2]]


# 1.删除列表中所有重复的元素(重复元素只保留一个)。
# 输入：[4,35,7,64,7,35]
# 输出：[4, 35, 7, 64]
# list01 = [4, 35, 7, 64, 7, 35]
# for r in range(len(list01) - 1, -1, -1):
#     for c in range(r):
#         if list01[r] == list01[c]:
#             del list01[r]
#             break
# print(list01)
# 2. 质数：大于1的整数，除了1和它本身以外不能再被其他数字整除。
#      获取指定范围内的所有质数。
# 输入：2,20
# 输出：[2, 3, 5, 7, 11, 13, 17, 19]
# start = int(input("请输入开始值："))  # 3
# stop = int(input("请输入结束值："))  # 9
# for number in range(start, stop):
#     for i in range(2, number):
#         if number % i == 0:
#             #print("不是素数")
#             break
#     else:
#         print(number)

# 3.  计算个人所得税
# 公式：个税 = （累计纳税工资*税率-速算扣除数）-累计已缴纳税额
# 	累计纳税工资 = 累计税前工资 -累计起征点- 累计专项扣除数- 累计社保

#获取数据
list_salary_before_tax = [30000]*12 # 税前收入工资
free_income = 5000 #免税收入（起征点）
base_pay =30000#社保缴纳基数
social_insurance = 3+ base_pay*(0.08+0.002+0.02+0.12)
specical_deduction = 1000 # 专项扣除数
list_tax = [] #个税列表 为了表示 每个月的个税
#逻辑处理
for i in range(len(list_salary_before_tax)): # 5----> 01234
    i+=1 #月份
#累计纳税工资 = 累计税前工资 -累计起征点- 累计专项扣除数- 累计社保
    salary_pay_tax = sum(list_salary_before_tax[:i]) -free_income*i-\
                     specical_deduction*i-social_insurance*i
    #计算税率和速算扣除数
    if salary_pay_tax<36000:
        tax_rate = 0.03
        deduction = 0
    elif salary_pay_tax<=144000:
        tax_rate = 0.1
        deduction = 2520
    elif salary_pay_tax<=300000:
        tax_rate = 0.2
        deduction = 16920
    elif salary_pay_tax<=420000:
        tax_rate = 0.25
        deduction = 31920
    elif salary_pay_tax <= 660000:
        tax_rate = 0.3
        deduction = 52920
    elif salary_pay_tax <=960000:
        tax_rate = 0.35
        deduction = 85920
    else:
        tax_rate = 0.45
        deduction= 181920
    #个税 = （累计纳税工资*税率-速算扣除数）-累计已缴纳税额
    tax = round((salary_pay_tax*tax_rate-deduction)-sum(list_tax),2)
    #如果本月应预扣缴纳额为负，暂不扣税
    if tax <0: tax=0
    list_tax.append(tax)
#输出结果
print(list_tax)

#round 保留指定精度的小数 round（1.23456,3）    1.234


name = "xixi" # name 对象
print(id(name)) # id ：身份的唯一标识
type(name) # 对象的类型，决定了该对象可以保存什么类型的值
print(name) # 对象的值，表示数据









