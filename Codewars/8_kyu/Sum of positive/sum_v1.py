from functools import reduce

def positive_sum(arr):
    return reduce(lambda x, y: x + y * (y > 0), arr, 0)
