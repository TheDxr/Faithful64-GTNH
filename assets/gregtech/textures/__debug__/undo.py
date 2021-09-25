# coding=utf-8
import shutil
import os


old_folder = '__debug__\\new'  # old folder name
new_folder = '__debug__\\old'  # new folder name
to_folder = 'materialicons'  # deploy to


def move(new_file, dst, old_file):
    try:
        if dst.split("\\")[-1] == old_file.split('\\')[-1] and os.path.getsize(dst) == os.path.getsize(old_file):
            print("MOVE : "+new_file+" ==> "+dst)
            print("MOVE : "+new_file+" ==> "+dst, file=history_file)
            shutil.copy2(new_file, dst)
    except FileNotFoundError as e:
        print(e)


def move_file(file_list, new_file, old_file):
    for file in file_list:
        if os.path.isdir(file):
            os.chdir(file)
            ls = os.listdir()
            move_file(ls, new_file, old_file)
            os.chdir(os.path.pardir)
        else:
            move(new_file, os.path.join(os.getcwd(), file), old_file)
    pass


os.system("cls")
history_file = open('__debug__\\history.txt', 'w')

# change to absoulte path
old_folder = os.path.join(os.getcwd(), old_folder)
new_folder = os.path.join(os.getcwd(), new_folder)
to_folder = os.path.join(os.getcwd(), to_folder)

# cheack file and replace
new_files = os.listdir(new_folder)
for new_file in new_files:
    os.chdir(to_folder)
    file_list = os.listdir()
    move_file(file_list, os.path.join(new_folder, new_file),
              os.path.join(old_folder, new_file))
