from src.Statistics.mean import mean
from src.Calculator.division import division
from src.Calculator.square import square
from src.Calculator.subtraction import subtraction
from src.Calculator.addition import addition


def variance(data):
    try:
        data_len = len(data)
        data_sum = 0
        data_mean = mean(data)
        for num in data:
            data_sum = addition(data_sum, square(subtraction(data_mean, num)))
        return division(data_len - 1, data_sum)
    except ValueError:
        print("error: value is not a number")
        return None
    except IndexError:
        print("error: list is empty")
        return None
    except ZeroDivisionError:
        print("error: cannot divide by zero")
        return None
