def find_next_square(sq):
    return -1 if (x := sq**0.5) % 1 else sq+x+x+1
