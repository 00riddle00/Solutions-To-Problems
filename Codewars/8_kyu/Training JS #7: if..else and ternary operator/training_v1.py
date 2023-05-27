def sale_hotdogs(n):
    return 100 * n if n < 5 else 95*n - 5*n*(n > 9)
