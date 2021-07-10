from src.Calculator.calculator import Calculator
from src.Statistics.mean import mean


class Statistics(Calculator):
    data = []

    def __init__(self, data):
        self.data = data
        super().__init__()

    def mean(self):
        self.result = mean(self.data)
        return self.result

