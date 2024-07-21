def alias_gen(f, l):
    try:
        return FIRST_NAME[f[0].upper()]+" "+SURNAME[l[0].upper()]
    except KeyError:
        return "Your name must start with a letter from A - Z."
