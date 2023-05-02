from functools import reduce
import operator

def get_volume_of_cuboid(*d):
    return reduce(operator.mul, [*d])
