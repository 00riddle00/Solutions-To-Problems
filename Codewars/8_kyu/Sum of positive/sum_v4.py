def positive_sum(a):
    return sum(x*(x>0) for x in a)
