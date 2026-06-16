class Binary:
  def __init__(self, left, operator, right):
    self.left = left
    self.operator = operator
    self.right = right

  def accept(self, visitor):
    return visitor.visit_binary(self)

class Grouping:
  def __init__(self, expression):
    self.expression = expression

  def accept(self, visitor):
    return visitor.visit_grouping(self)

class Literal:
  def __init__(self, value):
    self.value = value

  def accept(self, visitor):
    return visitor.visit_literal(self)

class Unary:
  def __init__(self, operator, right):
    self.operator = operator
    self.right = right

  def accept(self, visitor):
    return visitor.visit_unary(self)