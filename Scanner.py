import Token
import TokenType
import main

class Scanner:
  def __init__(self, source):
    self.tokens = []
    self.source = source

    self.start = 0
    self.current = 0
    self.line = 1

  def scan_tokens(self):
    while not self.is_at_end():
      self.start = self.current
      self.scan_token()

    self.tokens.append(Token(TokenType.EOF, "", None, self.line))
    return self.tokens

  def scan_token(self):
    c = self.advance()
    match c:
      case "(": 
        self.add_token(TokenType.LEFT_PAREN)
      case ")": 
        self.add_token(TokenType.RIGHT_PAREN)
      case "{": 
        self.add_token(TokenType.LEFT_BRACE)
      case "}": 
        self.add_token(TokenType.RIGHT_BRACE)
      case ",": 
        self.add_token(TokenType.COMMA)
      case ".": 
        self.add_token(TokenType.DOT)
      case "-": 
        self.add_token(TokenType.MINUS)
      case "+": 
        self.add_token(TokenType.PLUS)
      case "*": 
        self.add_token(TokenType.STAR)
      case ";": 
        self.add_token(TokenType.SEMI_COLON)

      case _:
        main.error(self.line, "error: unexpected character.")
    

  def is_at_end(self):
    return self.current >= len(self.source)
  
  def advance(self):  
    self.current += 1
    return self.source[self.current - 1]

  def add_token(self, type, literal=None):
    text = self.source[self.start:self.current]
    self.tokens.append(Token(type, text, literal, self.line))    


    