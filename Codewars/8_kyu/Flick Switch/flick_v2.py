def flick_switch(l,b=1):
    return [(b:=b^(x=="flick")) for x in l]
