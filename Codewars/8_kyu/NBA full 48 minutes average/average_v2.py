def nba_extrap(ppg, mpg):
    try: return round(48*ppg/mpg,1)
    except ZeroDivisionError: 0
