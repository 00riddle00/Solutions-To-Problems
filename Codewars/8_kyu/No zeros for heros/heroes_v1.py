
def no_boring_zeros(n):
    try:
        return int(str(n).strip('0'))
    except ValueError:
        return 0
