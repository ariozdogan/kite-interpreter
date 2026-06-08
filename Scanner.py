import token
import token_type
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

    self.tokens.append(token(token_type.EOF, "", None, self.line))
    return self.tokens

  def scan_token(self):
    c = self.advance()
    match c:
      # single-character lexemes
      case "(": 
        self.add_token(token_type.LEFT_PAREN)
      case ")": 
        self.add_token(token_type.RIGHT_PAREN)
      case "{": 
        self.add_token(token_type.LEFT_BRACE)
      case "}": 
        self.add_token(token_type.RIGHT_BRACE)
      case ",": 
        self.add_token(token_type.COMMA)
      case ".": 
        self.add_token(token_type.DOT)
      case "-": 
        self.add_token(token_type.MINUS)
      case "+": 
        self.add_token(token_type.PLUS)
      case "*": 
        self.add_token(token_type.STAR)
      case ";": 
        self.add_token(token_type.SEMI_COLON)

      # single/double character lexemes
      case "!":
        self.add_token(token_type.BANG_EQUAL) if self.match("=") else self.add_token(token_type.BANG)
      case "=":
        self.add_token(token_type.EQUAL_EQUAL) if self.match("=") else self.add_token(token_type.EQUAL)
      case "<":
        self.add_token(token_type.LESS_EQUAL) if self.match("=") else self.add_token(token_type.LESS)
      case ">":
        self.add_token(token_type.GREATER_EQUAL) if self.match("=") else self.add_token(token_type.GREATER)

      # comments begin with a slash as well
      case "/":
        if self.match("/"):
          while self.peek() != "\n" and not self.is_at_end():
            self.advance()
        else:
          self.add_token(token_type.SLASH)

      # blank spaces
      case " " | "\r" | "\t":
        pass
      case "\n":
        self.line += 1

      case _:
        main.error(self.line, "error: unexpected character.")
    

  def is_at_end(self):
    return self.current >= len(self.source)
  
  def advance(self):  
    self.current += 1
    return self.source[self.current - 1]

  def add_token(self, type, literal=None):
    text = self.source[self.start:self.current]
    self.tokens.append(token(type, text, literal, self.line))    

  def match(self, expected):
    if self.is_at_end():
      return False

    if self.source[self.current] != expected:
      return False
    
    self.current += 1
    return True
  
  def peek(self):
    if self.is_at_end():
      return "\0"
    return self.source[self.current]

    