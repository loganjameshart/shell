#!/usr/bin/env python3
import os
import sys
import shutil
import getpass


"""***---Environment variables, expressed as a dictionary.---***"""


ENV = {
    "PROMPT": "", 
    "USER": getpass.getuser()
}

COLOR = {
    "BLACK": "\033[0;30m",
    "RED": "\033[0;31m",
    "GREEN": "\033[0;32m",
    "BROWN": "\033[0;33m",
    "BLUE": "\033[0;34m",
    "PURPLE": "\033[0;35m",
    "CYAN": "\033[0;36m",
    "LIGHT_GRAY": "\033[0;37m",
    "DARK_GRAY": "\033[1;30m",
    "LIGHT_RED": "\033[1;31m",
    "LIGHT_GREEN": "\033[1;32m",
    "YELLOW": "\033[1;33m",
    "LIGHT_BLUE": "\033[1;34m",
    "LIGHT_PURPLE": "\033[1;35m",
    "LIGHT_CYAN": "\033[1;36m",
    "LIGHT_WHITE": "\033[1;37m",
    "BOLD": "\033[1m",
    "FAINT": "\033[2m",
    "ITALIC": "\033[3m",
    "UNDERLINE": "\033[4m",
    "BLINK": "\033[5m",
    "NEGATIVE": "\033[7m",
    "CROSSED": "\033[9m",
    "END": "\033[0m",
}


def color_print(color_choice: str, text: str) -> None:
    """Prints text in color according to ANSI codes in COLOR dictionary."""
    print(f"{COLOR[color_choice.upper()]}{text}{COLOR['END']}")


def update_prompt():
    """Updates prompt to current working directory. Used in main loop after every function call."""
    ENV[
        "PROMPT"
    ] = f"{COLOR['LIGHT_BLUE']}~${os.getcwd()}{COLOR['LIGHT_WHITE']} >>>>> {COLOR['END']}"


"""***---Shell functions.---***"""


def echo(arg: str = None) -> None:
    """USE: echo [string]. Prints string to stdout."""
    print(arg)


def export(arg: str = None) -> None:
    """USE: export [enviornment variable name] = [new environment variable value]. Sets environment variables for the current shell session."""
    variable, value = arg.split("=", maxsplit=1)
    if ENV[variable]:
        ENV[variable] = value
    else:
        print(f"{ENV['PROMPT']} Environment variable {variable} doesn't exist.")


def ls(arg: str = None) -> None:
    """USE: ls [directory]. Lists items in requested directory. Lists current directory if none is inputted."""
    try:
        if arg:
            directory_list = os.listdir(arg)
            directory_list.sort()
            for item in directory_list:
                if os.path.isdir(item):
                    color_print("cyan", item)
                elif os.path.isfile(item):
                    color_print("green", item)
                else:
                    print(item)
        else:
            directory_list = os.listdir()
            directory_list.sort()
            for item in directory_list:
                if os.path.isdir(item):
                    color_print("cyan", item)
                elif os.path.isfile(item):
                    color_print("green", item)
                else:
                    print(item)
    except Exception as e:
        print(e)


def clear() -> None:
    """USE: clear. Clears screen using system call depending on operating system."""
    command = "cls" if os.name == "nt" else "clear"
    os.system(command)


def pwd() -> None:
    """USE: pwd. Prints working directory."""
    print(os.getcwd())


def cd(arg: str) -> None:
    """USE: cd [directory]. Changes working directory."""
    cwd = os.getcwd()
    if os.path.isdir(arg):
        os.chdir(os.path.join(cwd, arg))
    else:
        print(f"{ENV['PROMPT']} '{arg}' is not a directory.")


def rm(arg: str) -> None:
    """USE: rm [file/directory]. Deletes file or directory. If directory is not empty, confirms deletion before proceeding."""
    if os.path.isdir(arg):
        if os.listdir(arg):
            decision = input(f"{ENV['PROMPT']}Are you sure you want to remove {arg}? y/n ")
            if decision.lower() == "y":
                shutil.rmtree(arg)
                print(f"{ENV['PROMPT']}Directory '{arg}' deleted.")
            else:
                print(f"{ENV['PROMPT']}Operation aborted.")
        else:
            shutil.rmtree(arg)
    else:
        os.remove(arg)


def mv(arg: str) -> None:
    """USE: mv [source] [destination]. Moves file from source argument to destination argument."""
    source, destination = arg.split(maxsplit=1)[0], arg.split(maxsplit=1)[1]
    shutil.move(source, destination)


def cp(arg: str) -> None:
    """USE: cp [source] [destination]. Copies file from source argument to destination argument."""
    source, destination = arg.split(maxsplit=1)[0], arg.split(maxsplit=1)[1]
    shutil.copy2(source, destination)


def mkdir(arg: str) -> None:
    """USE: mkdir [directory name]. Creates new directory in current working directory."""
    os.mkdir(arg)


def cat(arg: str) -> None:
    """USE: cat [file]. Reads file to stdout."""
    if not os.path.isfile(arg):
        print(f"{ENV['PROMPT']}'{arg}' is not a file. Can only read files to stdout.")
    with open(arg) as file:
        print(file.read())


def touch(arg: str) -> None:
    """USE: touch [file name]. Creates new blank file in current working directory."""
    open(arg, "a").close()


def help(arg: str = None) -> None:
    """USE: help [command]. Provides instructions for each command. If no command is listed, provides a list of available commands."""
    if arg:
        print(DISPATCH[arg].__doc__)
    else:
        print(f"{ENV['PROMPT']}Available commands:")
        for command in DISPATCH.keys():
            print(command)


def quit():
    """USE: quit. Quits shell."""
    sys.exit()


"""***---Dispatch control and main shell.---***"""


DISPATCH = {
    "echo": echo,
    "export": export,
    "ls": ls,
    "clear": clear,
    "pwd": pwd,
    "cd": cd,
    "rm": rm,
    "mv": mv,
    "cp": cp,
    "mkdir": mkdir,
    "touch": touch,
    "cat": cat,
    "help": help,
    "quit": quit,
}


def execute_command(called_function, arg=None):
    """Executes command based upon dispatch table. Passes argument if one is required."""
    try:
        if arg:
            DISPATCH[called_function](arg)
        else:
            DISPATCH[called_function]()
    except Exception as e:
        print(
            f"{ENV['PROMPT']} Command {called_function} not found. Enter 'help' to see a list of available commands."
        )


def main():
    """Main shell loop."""
    while True:
        update_prompt()

        command = input(f"{ENV['PROMPT']}")
        split_command = command.split(" ", maxsplit=1)
        if len(split_command) == 2:
            function = split_command[0]
            argument = split_command[1]
            execute_command(function, arg=argument)
        else:
            function = split_command[0]
            execute_command(function)


if __name__ == "__main__":
    main()
