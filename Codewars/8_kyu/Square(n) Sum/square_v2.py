from itertools import repeat

def square_sum(ns):
    return sum(map(pow, ns, repeat(2)))
