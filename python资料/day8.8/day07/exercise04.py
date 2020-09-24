"""
    行数4     列数
    *          1
    **         2
    ***        3
    ****       4
"""
for r in range(4):#        0     1    r
    for c in range(r+1):#  1     2   r+1
        print("*",end = "")
    print()