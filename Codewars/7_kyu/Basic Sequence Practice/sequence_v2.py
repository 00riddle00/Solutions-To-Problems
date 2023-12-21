def sum_of_n(n):
    return [[-1,1][n>0]*sum(range(i+1)) for i in range(abs(n)+1)]
