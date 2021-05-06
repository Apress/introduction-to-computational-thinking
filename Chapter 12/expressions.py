import math
from abc import ABC, abstractmethod

class Constant(object):
    def __init__(self, value):
        self.value = value
    def evaluate(self):
        return self.value
    def __repr__(self):
        return "Constant(" + repr(self.value) + ")"
    def __str__(self):
        return str(self.value)

class UnaryOp(ABC):
    def __init__(self, expr):
        self.expr = expr

    def evaluate(self):
        return self.apply(self.expr.evaluate())
    @abstractmethod
    def apply(self, value):
    	pass

    def __repr__(self):
        name = self.__class__.__name__
        return name + "(" + repr(self.expr) + ")"
    def __str__(self):
        format_string = self.format_string
        return self.format_string.format(str(self.expr))

class BinaryOp(ABC):
    def __init__(self, left, right):
        self.left, self.right = left, right

    def evaluate(self):
        return self.apply(self.left.evaluate(),
					      self.right.evaluate())
    @abstractmethod
    def apply(self, left, right):
    	pass

    def __repr__(self):
        name = self.__class__.__name__
        return name + "(" + repr(self.left) + ", " \
                          + repr(self.right) + ")"
    def __str__(self):
        op = self.op
        return "(" + str(self.left) + op + str(self.right) + ")"

class Minus(UnaryOp):
    format_string = "-{}"
    def apply(self, value):
        return - value

class Exp(UnaryOp):
    format_string = "exp({})"
    def apply(self, value):
        return math.exp(value)

class Add(BinaryOp):
    op = "+"
    def apply(self, left, right):
        return left + right

class Sub(BinaryOp):
    op = "-"
    def apply(self, left, right):
        return left - right

expr = Add(Minus(Constant(2)), Sub(Exp(Constant(42)), Constant(13)))
print(expr)
print(expr.evaluate())
