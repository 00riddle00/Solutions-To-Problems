from math import isclose

def approx_equals(a, b):
    return isclose(a, b, rel_tol=0, abs_tol=1e-3)
