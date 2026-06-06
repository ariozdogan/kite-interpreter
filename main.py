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

class TokenType(Enum):
    # single-character tokens
    LEFT_PAREN  = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE  = auto()
    RIGHT_BRACE = auto()
    COMMA       = auto()
    DOT         = auto()
    MINUS       = auto()
    PLUS        = auto()
    STAR        = auto()
    SLASH       = auto()
    SEMICOLON   = auto()

    # one/two character tokens
    BANG          = auto()
    BANG_EQUAL    = auto()
    EQUAL         = auto()
    EQUAL_EQUAL   = auto()
    GREATER       = auto()
    GREATER_EQUAL = auto()
    LESS          = auto()
    LESS_EQUAL    = auto()

    # literals
    IDENTIFIER = auto()
    STRING     = auto()
    NUMBER     = auto()

    # keywords
    AND    = auto()
    CLASS  = auto()
    ELSE   = auto()
    FALSE  = auto()
    FUN    = auto()
    FOR    = auto()
    IF     = auto()
    NULL   = auto()
    OR     = auto()
    PRINT  = auto()
    RETURN = auto()
    SUPER  = auto()
    THIS   = auto()
    TRUE   = auto()
    STR    = auto()
    INT    = auto()
    FLOAT  = auto()
    BOOL   = auto()
    WHILE  = auto()

    EOF = auto()

def main():
    if sys.argv > 2:
        print("too many arguments")
    
    elif sys.argv == 2:
        run_file(sys.argv[1])
    else:
        run_prompt()


    return


