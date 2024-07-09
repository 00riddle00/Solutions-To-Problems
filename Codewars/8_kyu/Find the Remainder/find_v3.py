def remainder(a,b):
    return abs(a-b) % min(a,b) if min(a,b) else None
