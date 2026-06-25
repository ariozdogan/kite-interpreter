from expressions import Binary, Grouping, Literal, Unary
from token_type import TokenType
from kite_token import Token

class ExpressionPrinter:
    def print(self, expression):
        return expression.accept(self)

    def visit_literal(self, expression):
        if expression.value is None:
            return "nil"
        return str(expression.value)

    def visit_grouping(self, expression):
        return self.parenthesize("group", expression.expression)

    def visit_unary(self, expression):
        return self.parenthesize(expression.operator.lexeme, expression.right)

    def visit_binary(self, expression):
        return self.parenthesize(expression.operator.lexeme, expression.left, expression.right)

    def parenthesize(self, name, *exprs):
        parts = ["(", name]
        for expr in exprs:
            parts.append(" ")
            parts.append(expr.accept(self))
        parts.append(")")
        return "".join(parts)
    
def main():
    left = Unary(Token(TokenType.MINUS, "-", None, 1), Literal(123))
    operator = Token(TokenType.STAR, "*", None, 1)
    right = Grouping(Literal(45.67))

    printer = ExpressionPrinter()
    expression = Binary(left, operator, right)

    print(printer.print(expression))



main()

    
