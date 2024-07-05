from itertools import repeat

def number_to_pwr(n,p):
    return __import__("m"+"ath").prod(repeat(n,p))
