def number_to_pwr(n,p):
    return n * number_to_pwr(n,p-1) if p else 1
