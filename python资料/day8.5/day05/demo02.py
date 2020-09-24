"""
    切片
        容器[整数:整数:整数]
        定位多个数据
"""
# 为了生成整数
# for item in range(1,5,1):
#     print(item)

message = "我是齐天大圣孙悟空"

# 写法1:容器名[开始:结束:间隔]
# 注意:不包含结束
print(message[1:5:1])  # 是是齐天大

# 写法2:容器名[开始:结束]
# 注意:间隔默认为1
print(message[1:5])  # 是是齐天大

# 写法3:容器名[:结束]
# 注意:开始默认为头
print(message[:5])  # 我是齐天大

# 写法4:容器名[:]
# 注意:结束默认为尾
# 圣孙悟空

# 特殊1:没有越界
print(message[:100])  # 我是齐天大圣孙悟空
# 特殊2:反转
print(message[::-1])  # 空悟孙圣大天齐是我

message = "我是齐大圣孙悟空"

# 训练
# print(message[2: 6])# 齐天大圣
print(message[2: -3])  # 齐天大圣
print(message[3: -1])  # 天圣孙悟
print(message[2:: -1])# 齐是我
print(message[1:4:-1])# 空

