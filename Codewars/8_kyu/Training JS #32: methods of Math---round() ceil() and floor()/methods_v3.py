from math import ceil

def round_it(n):
    l, r = (len(x) for x in str(n).split("."))
    return ceil(n) if l < r else int(n) if l > r else round(n)
