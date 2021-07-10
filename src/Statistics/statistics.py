from src.Calculator.calculator import Calculator
from src.Statistics.mean import mean
from src.Statistics.variance import variance
from src.Statistics.std_dev import standarddev


class Statistics(Calculator):
    data = []

    def __init__(self, data):
        self.data = data
        super().__init__()

    def mean(self):
        self.result = mean(self.data)
        return self.result

    def variance(self):
        self.result = variance(self.data)
        return self.result

    def standarddev(self):
        self.result = standarddev(self.data)
        return self.result

