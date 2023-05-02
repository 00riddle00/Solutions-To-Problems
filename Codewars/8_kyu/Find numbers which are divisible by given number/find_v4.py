def divisible_by(n,d):
    return [*filter(lambda x: not x%d, n)]
