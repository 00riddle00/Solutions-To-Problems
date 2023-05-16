def quadrant(x,y):
    return [1+2*(x<0),2+2*(x>0)][x*y<0]
