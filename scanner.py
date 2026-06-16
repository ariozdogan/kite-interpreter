import token
import token_type
import kite
import static_keywords

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

      # quote
      case '"':
        self.string()

      case _:
        if self.is_digit(c):
          self.number()
        elif self.is_alpha(c):
          self.identifier()
    
        else:
          kite.error(self.line, "unexpected character.")
    

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
  
  def string(self):
    while self.peek() != '"' and not self.is_at_end():
      if self.peek() == "\n":
        self.line += 1

      self.advance()

    if self.is_at_end():
      kite.error(self.line, "unterminated string")
      return

    self.advance()
    string_value = self.source[(self.start + 1):(self.current - 1)]
    self.add_token(token_type.STRING, string_value)

  def is_digit(self, c):
    return c >= "0" and c <= "9"
  
  def number(self):
    while self.is_digit(self.peek()):
      self.advance()
    
    if self.peek() == "." and self.is_digit(self.peekNext()):
      self.advance()

      while self.is_digit(self.peek()):
        self.advance()
    
    self.add_token(token_type.NUMBER, float(self.source[self.start:self.current]))

  def peekNext(self):
    if (self.current + 1) >= len(self.source):
      return "\0"
    return self.source[self.current + 1]
  
  def is_alpha(self, c):
    return (c >= "a" and c <= "z") or (c >= "A" and c <= "Z") or (c == "_") 
  
  def is_alpha_numeric(self, c):
    return self.is_alpha(c) or self.is_digit(c)
  
  def identifier(self):
    while self.is_alpha_numeric(self.peek()):
      self.advance()
    
    text = self.source[self.start:self.current]
    type = static_keywords.keywords.get(text)

    if type == None:
      type = token_type.IDENTIFIER

    self.add_token(type)
    
