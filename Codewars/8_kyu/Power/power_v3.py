from itertools import repeat
from functools import reduce
from operator import mul

def number_to_pwr(n,p):
    return reduce(mul, repeat(n,p), 1)
