def string_clean(s):
    return "".join(filter(lambda c: not c.isdigit(), s))
