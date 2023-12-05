import operator
from functools import reduce

logical_calc = lambda arr, op: reduce(operator.__dict__[f"__{op.lower()}__"], arr)
