from functools import reduce

def grow(arr):
    return reduce(int.__mul__, arr)
