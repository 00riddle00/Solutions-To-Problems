def get_sum(a, b):
    # Sum = (first + last) * n / 2
    # ^-- comes from arithmetic progression.
    return (a + b) * (abs(a - b) + 1) // 2
