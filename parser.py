from scanner import Scanner
from token_type import TokenType
from expressions import Binary

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def expression():
        return equality()
    
    def equality():
        expr = comparison()  

        while(Scanner.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL)):
            operator = previous()
            right = comparison()
            expression = Binary(expression, operator, right)

        return expression
