import sys
from enum import Enum, auto

source = None
path = None


def run(source):
    pass

def run_file(path):
    file_object = open(path, mode='r', encoding=None)
    return file_object

def run_prompt():
    while(True):
        try:
            user_arg = input("kite <<<")
            return user_arg
        except EOFError:
            break

def error(line, message):
    report(line, "", message)

def report(line, where, message):
    print(where + ", line: " + line)
    print("Error: "+ message)

    hadError = True

def main():
    if sys.argv > 2:
        print("too many arguments")
    
    elif sys.argv == 2:
        run_file(sys.argv[1])
    else:
        run_prompt()


    return


