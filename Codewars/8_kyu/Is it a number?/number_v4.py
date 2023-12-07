def isDigit(s):
    try: return bool(float(s)) or 1
    except: return 0
