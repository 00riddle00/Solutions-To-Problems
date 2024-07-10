def neutralise(v,w):
    return "".join("0" if x!=y else x for x,y in zip(v,w))
