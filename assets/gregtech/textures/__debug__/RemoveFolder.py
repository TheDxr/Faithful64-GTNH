# coding=utf-8
import shutil
import os


def move(src, dst):
    ls = os.listdir(os.path.pardir)
    dst_2 = dst.split('\\')
    if dst_2[-1] in ls and os.path.getsize(dst) != os.path.getsize(src):
        dst = dst[0:-4] + '-' + dst[-4:-1] + dst[-1]
        move(src, dst)
        return
    print("MOVE : "+src+" TO "+dst)
    print("MOVE : "+src+" TO "+dst,file=history)
    shutil.move(src, dst)



def move_file(file_list, depth):
    for file in file_list:
        if os.path.isdir(file):
            os.chdir(file)
            ls = os.listdir()
            move_file(ls, depth+1)
            os.chdir(os.path.pardir)
        else:
            # for i in range(depth):
            #     print(" - ",end="")
            # print(file)
            move(os.path.join(os.getcwd(), file),
                 os.path.join(parent_dir, file))
    pass

history = open('history.txt','a+')
cwd = os.listdir()
parent_dir = os.getcwd()
cwd_2 = []
for folder in cwd:
    if os.path.isdir(folder):
        cwd_2.append(folder)

move_file(cwd_2, 0)
for i in cwd_2:
    shutil.rmtree(i)
os.system('cls')
print('done')
