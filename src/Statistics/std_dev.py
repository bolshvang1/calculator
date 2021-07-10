from src.Calculator.squareroot import squareroot
from src.Statistics.variance import variance


def standarddev(data):
    try:
        var = variance(data)
        return squareroot(var)
    except ValueError:
        print("error: value is not a number")
        return None
    except IndexError:
        print("error: list is empty")
        return None
    except ZeroDivisionError:
        print("error: cannot divide by zero")
        return None