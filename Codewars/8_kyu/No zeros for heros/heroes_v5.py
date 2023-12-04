
def no_boring_zeros(n):
    while n and n % 10 == 0:
        n /= 10
    return n
