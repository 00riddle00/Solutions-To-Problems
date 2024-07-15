def draw_stairs(n):
    return "\n".join("I".rjust(i+1) for i in range(n))
