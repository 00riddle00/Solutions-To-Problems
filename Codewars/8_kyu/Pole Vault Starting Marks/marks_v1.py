def starting_mark(height):
    slope = (10.67 - 9.45) / (1.83 - 1.52)
    return round((9.45 + slope*(height-1.52)), 2)
