import re

def abbrev_name(n):
    return re.sub("^(\w).* (\w).*", "\\1.\\2", n).upper()
