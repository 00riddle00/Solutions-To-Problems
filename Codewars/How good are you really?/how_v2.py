from statistics import mean

def better_than_average(cp, yp):
    return yp > mean(cp + [yp])
