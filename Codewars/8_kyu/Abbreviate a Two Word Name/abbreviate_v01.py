def abbrev_name(name):
    return '.'.join([x.upper() for x in [name.split()[0][0], name.split()[1][0]]])
