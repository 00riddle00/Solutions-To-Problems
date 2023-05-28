import math

def calculate_tip(n,r):
    return math.ceil(n * d[r] / 100) if (r:=r.lower()) in (d:={"terrible":0, "poor":5, "good":10, "great":15, "excellent":20}) else "Rating not recognised"
