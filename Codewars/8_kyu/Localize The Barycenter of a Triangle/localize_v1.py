def bar_triang(point_a, point_b, point_c):
    xa,ya,xb,yb,xc,yc = point_a + point_b + point_c
    return [round((xa+xb+xc)/3,4), round((ya+yb+yc)/3,4)]
