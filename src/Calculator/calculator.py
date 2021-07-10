from src.Calculator.addition import addition
from src.Calculator.subtraction import subtraction
from src.Calculator.multiplication import multiplication
from src.Calculator.division import division
from src.Calculator.square import square
from src.Calculator.squareroot import squareroot


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def squareroot(self, a):
        self.result = squareroot(a)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result
