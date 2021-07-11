from src.Calculator.subtraction import subtraction
from src.Calculator.addition import addition
from src.Calculator.division import division


def median(data):
    try:
        data_len = len(data)
        data.sort()
        if data_len % 2 == 0:
            median1 = data[data_len // 2]
            median2 = data[int(subtraction(1, data_len // 2))]
            median = division(2, addition(median1, median2))
        else:
            median = data[data_len // 2]
        return median
    except ValueError:
        print("error: value is not a number")
        return None
    except IndexError:
        print("error: list is empty")
        return None
    except ZeroDivisionError:
        print("error: cannot divide by zero")
        return None