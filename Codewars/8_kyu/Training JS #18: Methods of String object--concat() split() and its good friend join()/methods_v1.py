def split_and_merge(s, sep):
    return " ".join(sep.join(x) for x in s.split())
