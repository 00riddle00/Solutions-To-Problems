import re

def abbrev_name(n):
    return '.'.join(re.findall(r'\b\w', n.title()))
