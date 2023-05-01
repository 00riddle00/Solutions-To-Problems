from operator import mul
from functools import reduce

def grow(arr):
    return reduce(mul, arr, 1)
