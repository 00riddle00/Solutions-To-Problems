def square_or_square_root(a):
    return [x**(2 if x**.5 % 1 else .5) for x in a]
