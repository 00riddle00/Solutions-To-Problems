def get_nth(n):
    sign = 1 if n > 0 else -1
    nth = 0
    for idx in range(abs(n) + 1):
        nth += sign * idx
        yield nth


def sum_of_n(n):
    return [*get_nth(n)]
