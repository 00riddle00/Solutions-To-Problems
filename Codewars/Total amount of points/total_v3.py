def points(g):
    return sum(3*(x[0]>x[2])+(x[0]==x[2]) for x in g)
