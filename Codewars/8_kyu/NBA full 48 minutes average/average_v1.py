def nba_extrap(ppg, mpg):
    return round(48*ppg/mpg,1) if mpg else 0
