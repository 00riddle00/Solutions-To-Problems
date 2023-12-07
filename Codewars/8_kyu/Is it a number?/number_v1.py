def isDigit(s):
    try:
        float(s)
        return 1
    except: return 0
