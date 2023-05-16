def next_item(xs,item,f=0):
    for x in xs:
        if f: return x
        f = (x==item)
