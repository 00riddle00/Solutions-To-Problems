def find_next_square(sq):
    return (x+1)**2 if sq == (x := int(sq**0.5))**2 else -1
