def stringy(size):
    return '10' * (size >> 1) + '1' * (size & 1)
