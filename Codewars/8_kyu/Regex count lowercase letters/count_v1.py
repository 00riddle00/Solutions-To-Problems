import re

def lowercase_count(s):
    return len(re.findall("[a-z]", s))
