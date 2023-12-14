import math

def circle_area(r):
    if r <= 0:
        raise ValueError
    return round(math.pi * r**2, 2)
