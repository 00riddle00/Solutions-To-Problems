def sale_hotdogs(n):
    return n * (100 if n < 5 else 95 - 5 * (n > 9))
