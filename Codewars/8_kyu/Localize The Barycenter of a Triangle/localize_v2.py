def bar_triang(point_a, point_b, point_c):
    return [round(sum(x)/3.0, 4) for x in zip(point_a,point_b,point_c)]
