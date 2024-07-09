def flick_switch(l,b=1):
    return [(b:=b^1) if x=="flick" else b for x in l]
