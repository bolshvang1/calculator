from Calculator.addition import addition
from Calculator.division import division


def mean(data):
    data_len = len(data)
    data_sum = 0
    for num in data:
        data_sum = addition(data_sum, num)
    return division(data_len, data_sum)
