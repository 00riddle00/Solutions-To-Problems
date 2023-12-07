import re

def isDigit(s):
    return bool(re.match(r"^-?\d+\.?\d*?$", s))
