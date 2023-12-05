def logical_calc(arr, op):
    return eval(f" {op.replace('XOR','^').lower()} ".join(map(str,arr)))
