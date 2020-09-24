"""
练习2 :  使用进程池完成
拷贝一个指定的文件夹(该文件夹下没有子目录,全是普通文件)

思路提示: os.mkdir("xxx") 创建一个文件夹
         os.listdir('xxx') 获取文件列表

         把每个文件的拷贝作为进程池要执行的一个事件

         本质将源文件夹中所有文件拷贝到新文件夹
"""

from multiprocessing import Pool,Queue
import os

q = Queue() # 消息队列

# 进程池要做的的事件---拷贝文件
def copy(filename,old_folder,new_folder):
    fr = open(old_folder+'/'+filename,'rb')
    fw = open(new_folder+'/'+filename,'wb')
    while True:
        data = fr.read(1024 * 10)
        if not data:
            break
        n = fw.write(data) # 返回值就是写入大小
        q.put(n) #　存入消息队列
    fr.close()
    fw.close()

# 获取文件夹总大小
def get_size(dir):
    total_size = 0
    for file in os.listdir(dir):
        total_size += os.path.getsize(dir+'/'+file)
    return  total_size


# 创建进程池,执行事件
def main():
    # 获取文件列表
    old_folder = input("要拷贝的目录:")
    filelist = os.listdir(old_folder)
    os.mkdir(old_folder+'-备份')
    new_folder = old_folder+'-备份'

    # 文件夹大小
    total_size = get_size(old_folder)

    pool = Pool(4) # 创建进程池

    for file in filelist:
        pool.apply_async(func = copy,
                         args=(file,old_folder,new_folder))

    pool.close()

    copy_size = 0 #　已经拷贝的大小
    while copy_size < total_size:
        copy_size += q.get() # 从消息队列拿到已经拷贝的大小
        print("拷贝 %.2f%%"%(copy_size/total_size*100))


    pool.join()

if __name__ == '__main__':
    main()

