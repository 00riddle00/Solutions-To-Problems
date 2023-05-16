def number_to_pwr(n,p,a=1):
    for _ in range(1,p+1): a *= n
    return a
