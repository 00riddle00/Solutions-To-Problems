def round_it(n):
    l, r = map(len, str(n).split('.'))
    return round(n) if l == r else int(n) + (l < r)
