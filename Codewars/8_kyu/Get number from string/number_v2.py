import re

def get_number_from_string(s):
    return int("".join(re.findall("\d", s)))
