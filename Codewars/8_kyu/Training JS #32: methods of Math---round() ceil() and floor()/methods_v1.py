def round_it(n):
    l = str(n).index(".") - len(str(n)) / 2 + 0.5
    l = (l < 0) - (l > 0) # reversed "sign" function
    return round(n + 0.5 * l) # left: l=1, right: l=-1, middle: l=0
