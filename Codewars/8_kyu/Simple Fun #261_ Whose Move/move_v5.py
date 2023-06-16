def whoseMove(lastPlayer, win):
    return (a:=["white","black"])[a.index(lastPlayer) ^ (not win)]
