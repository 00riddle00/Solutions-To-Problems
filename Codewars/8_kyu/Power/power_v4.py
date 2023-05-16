from functools import reduce

def number_to_pwr(n,p):
    return reduce(int.__mul__, [n]*p, 1)
