from functools import reduce

def logical_calc(arr, op):
    return reduce(eval(f"bool.__{op.lower()}__"),arr)
