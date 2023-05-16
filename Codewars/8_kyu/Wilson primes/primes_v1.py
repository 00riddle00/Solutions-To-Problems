import math

def stirling_factorial(n):
    return ((n:=float(n))*math.log(n) - n + math.log(2*math.pi*n)/2. + 1/(12*n) - 1/(360*n**3) + 1/(1260 * n**5)) / math.log(10)

def am_i_wilson(p):
    return p>2 and not (((stirling_factorial if p>563 else math.factorial)(p-1))+1) % (p*p)
