def isValid(f):
    a,b,c,d,e,f,g,h = (x in f for x in range(1,9))
    return all([a+b!=2,c+d!=2,e==f,g+h])
