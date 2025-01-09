#!/usr/bin/env python3
import os
import sys
import shutil




def ls(arg=os.getcwd()):
    directory_list = os.listdir(arg)
    for item in directory_list:
        print(item)


def cd(arg):
    os.chdir(arg)


def rm(arg):
    if os.path.isdir(arg):
        os.rmdir(arg)
    os.remove(arg)


def mv(source, destination):
    shutil.move(source, destination)


def cp(source, destination):
    shutil.copy2(source, destination)


def mkdir(arg):
    os.mkdir(arg)


def touch(arg):
    new_file = open(arg)
    new_file.close()


def leave():
    sys.exit()


DISPATCH = {
    "ls": ls,
    "cd": cd,
    "rm": rm,
    "mv": mv,
    "cp": cp,
    "mkdir": mkdir,
    "touch": touch,
    "exit": leave
}


def run_function(called_function, arg=None):
    try:
        if arg:
            DISPATCH[called_function](arg)
        else:
            DISPATCH[called_function]
    except Exception as e:
        print(e)


def main():
    while True:
        cwd = os.getcwd()
        command = input(f"~${cwd} >>>>> ")
        split_command = command.split(' ', maxsplit=1)
        if len(split_command) == 2:
            function = split_command[0]
            argument = split_command[1]
            run_function(function, arg=argument)
        else:
            function = split_command[0]
            run_function(function)


if __name__ == "__main__":
    main()