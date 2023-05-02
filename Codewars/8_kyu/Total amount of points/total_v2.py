def pts(game):
    if game[0]>game[2]:
        return 3
    elif game[0]==game[2]:
        return 1
    else:
        return 0

def points(games):
    return sum(map(pts,games))
