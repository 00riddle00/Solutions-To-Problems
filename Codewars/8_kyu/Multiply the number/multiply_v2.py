def multiply(n):
    return n*5**(len(str(n))*(n>0) or len(str(n))-1)
