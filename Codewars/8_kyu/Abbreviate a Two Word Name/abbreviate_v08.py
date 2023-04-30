import re

def abbrev_name(n):
    return re.sub("(.).* (.).*", r"\1.\2", n.upper())
