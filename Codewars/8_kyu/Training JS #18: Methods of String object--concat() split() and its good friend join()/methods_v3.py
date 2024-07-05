import re

def split_and_merge(s, sep):
    return re.sub(r"(?<=\S)(?=\S)", sep, s)
