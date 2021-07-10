from src.Calculator.addition import addition
from src.Calculator.division import division


def mean(data):
    try:
        data_len = len(data)
        data_sum = 0
        for num in data:
            data_sum = addition(data_sum, num)
        return division(data_len, data_sum)
    except ValueError:
        print("error: value is not a number")
        return None
    except IndexError:
        print("error: list is empty")
        return None
    except ZeroDivisionError:
        print("error: cannot divide by zero")
        return None
