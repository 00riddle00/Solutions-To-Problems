from itertools import count

def find_next_square(x):
    if x == int(x**0.5)**2:
        return next(y for y in count(x+1) if y == int(y**0.5)**2)
    else:
        return -1
