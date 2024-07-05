def uefa_euro_2016(t,s):
    return f"At match {' - '.join(t)}, {f"{t[d<0]} won!" if (d:=s[0]-s[1]) else 'teams played draw.'}"
