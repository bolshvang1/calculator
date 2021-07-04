from CsvReader import CsvReader
import math


def addition(a, b):
    c = int(a) + int(b)
    return c


def subtraction(a, b):
    c = int(b) - int(a)
    return c


def multiplication(a, b):
    c = int(b) * int(a)
    return c


def squareroot(a):
    c = math.sqrt(float(a))
    return c


def division(a, b):
    c = float(b) / float(a)
    return c


def mean(data):
    mean = data
    return mean


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



class CSVStats(Calculator):
    data = []

    def __init__(self, data_file):
        self.data = CsvReader(data_file)
        pass

    def mean(self):
        mean(self.data)