# coding=utf-8
import shutil
import os


old_folder = '__debug__\\old'  # old folder name
new_folder = '__debug__\\new'  # new folder name
to_folder = '__debug__\\material'  # deploy to


def move(new_file, dst, old_file):
    try:
        if os.path.getsize(dst) == os.path.getsize(old_file):
            print("MOVE : "+new_file+" TO "+dst)
            print("MOVE : "+new_file+" TO "+dst, file=history_file)
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
