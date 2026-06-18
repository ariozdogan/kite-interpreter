from scanner import Scanner
from token_type import TokenType
from expressions import Binary, Unary, Literal, Grouping

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens # stores list of tokens
        self.current = 0 # points to the next token that will be parsed

    def expression(self):
        return self.equality()
    
    def equality(self): 
        expression = self.comparison() 

        while self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            operator = self.previous()
            right = self.comparison()
            expression = Binary(expression, operator, right)

        return expression
    
    def comparison(self): 
        expression = self.term()

        while self.match(TokenType.GREATER, TokenType.GREATER_EQUAL, TokenType.LESS, TokenType.LESS_EQUAL):
            operator = self.previous()
            right = self.term()
            expression = Binary(expression, operator, right)

        return expression
    
    def term(self):
        expression = self.factor()

        while self.match(TokenType.PLUS, TokenType.MINUS):
            operator = self.previous()
            right = self.factor()
            expression = Binary(expression, operator, right)

        return expression
    
    def factor(self):
        expression = self.unary()

        while self.match(TokenType.STAR, TokenType.SLASH):
            operator = self.previous()
            right = self.unary()
            expression = Binary(expression, operator, right)

        return expression

    def unary(self):
        if self.match(TokenType.BANG, TokenType.MINUS):
            operator = self.previous()
            right = self.unary()
            return Unary(operator, right)
        
        return self.primary()
    

    def primary(self): # parses highest presedence literals
        if self.match(TokenType.FALSE):
            return Literal(False)
        
        if self.match(TokenType.TRUE):
            return Literal(True)
        
        if self.match(TokenType.NULL):
            return Literal(None)
        
        if self.match(TokenType.NUMBER, TokenType.STRING):
            return Literal(self.previous())
        
        if self.match(TokenType.LEFT_PAREN):
            expression = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Expect ')' after expression")

            return Grouping(expression)
    
    def match(self, *args): # checks if current token is a given type
        for type in args:
            if self.check(type):
                self.advance()
                return True
            
        return False
    
    def check(self, type): # checks current token's type without consuming
        if self.is_at_end():
            return False
        
        return self.peek().type == type

    def advance(self):  # consumes token and returns it
        if not self.is_at_end():
            self.current += 1

        return self.previous()
    
    def is_at_end(self): # checks if there are more tokens to parse
        return self.peek().type == TokenType.EOF
    
    def peek(self): # the current token that is yet to be consumed
        return self.tokens[self.current]
    
    def previous(self): # the token that was just consumed
        return self.tokens[self.current - 1]

