def sum_array(a):
    return sum(a)-min(a)-max(a) if a and len(a) > 2 else 0
