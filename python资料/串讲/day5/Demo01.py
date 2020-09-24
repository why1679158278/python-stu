"""
# 学生信息管理系统   课后练习
要求：请用户选择序号1-4，分别代表不同的选项
用户可以无线输入学生信息（姓名 年龄 QQ 地址），
如果选择1：需要输入4个信息分别是 姓名 年龄 QQ 地址
        2：用户只需要输入名字，你就要显示学生的四个信息
        3：你需要将前面用户输入的学员信息都显示出来
        4：退出输入系统

这道题是综合应用，用到循环 选择语句 列表 字典（仅供参考）

"""
print("="*50)
print("学生管理系统0.1版")
print("1.添加一个新学生信息")#学生信息包含姓名 年龄 QQ 地址
print("2.查询某个学生信息")
print("3.显示所有学生信息")
print("4.退出系统")
print("="*50)
card_student_massage=[]
while True:
    #获取用户输入
    num = int(input("请输入操作序号"))
    if num==1: #根据用户的功能录入学生的信息
        _name = input("请输入名字")
        _age = input("请输入年龄")
        _qq = input("请输入QQ")
        _address = input("请输入地址")
        #定义一个字典存储一个学生的信息
        new_dic01 = {}
        new_dic01['name'] = _name
        new_dic01['age' ] = _age
        new_dic01['qq'] = _qq
        new_dic01['address'] = _address
        card_student_massage.append(new_dic01)
    elif num==2:
        find_name = input("请输入查找的学生姓名")
        find_flag = 0 #默认没找到
        for i in card_student_massage:
            if find_name ==i["name"]: #找到了该学生
                print("%s\t %s \t %s \t %s"%(i['name'],i['age'],i['qq'],i['address']))
                find_flag =1
                break
        if find_flag==0:
            print("查无此人")
    elif num ==3:
        print("姓名\t 年龄\t qq \t 地址")
        for item in card_student_massage:
            print("%s\t %s \t %s \t %s" % (item['name'], item['age'], item['qq'], item['address']))

    elif num==4:
        break
    else:
        print("您输入有误，请重新输入")
























