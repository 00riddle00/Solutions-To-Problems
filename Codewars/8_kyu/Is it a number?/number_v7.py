import re

def isDigit(s):
    return bool(re.match('^-?[\d\.]+$', s))
