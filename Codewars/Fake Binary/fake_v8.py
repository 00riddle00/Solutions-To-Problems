import re

def fake_bin(seq):
    return  re.sub("[5-9]", "1", re.sub("[0-4]", "0", seq))
