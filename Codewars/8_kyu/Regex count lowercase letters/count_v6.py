from functools import reduce

def lowercase_count(s):
    return reduce(lambda acc,c: acc + c.islower(), s, 0)
