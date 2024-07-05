from math import dist

def distance_between_points(a, b):
    return dist((a.x, a.y), (b.x, b.y))
