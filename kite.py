import sys
from enum import Enum, auto
from token_type import TokenType
from kite_token import Token
from parser import Parser
from expression_printer import ExpressionPrinter

source = None
path = None
had_error = False

def run(source, tokens):
    parser = Parser(tokens)
    expression = parser.parse()

    if had_error:
        return
    
    print(ExpressionPrinter.print(expression))
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

def report(line, where, message):
    print(where + ", line: " + line)
    print("Error: "+ message)

    hadError = True

def error(token, message):
    if Token.type == TokenType.EOF:
        report(Token.line, " at end", message)
    else:
        report(Token.line, "at '" + token.lexeme + "'", message)

def main():
    if sys.argv > 2:
        print("too many arguments")
    
    elif sys.argv == 2:
        run_file(sys.argv[1])
    else:
        run_prompt()


    return


