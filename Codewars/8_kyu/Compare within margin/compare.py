def close_compare(a, b, m=0):
    return (2*(a>b)-1)*(abs(a-b)>m)
