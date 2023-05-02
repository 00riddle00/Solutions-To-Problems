def points(games):
    sum = 0
    for g in games:
        if g[0] > g[2]:
            sum += 3
        elif g[0] == g[2]:
            sum += 1
    return sum
