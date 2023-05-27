def round_it(n):
    l, r = str(n).split('.')
    return round(n) if len(l) == len(r) else int(l) + (len(l) < len(r))
