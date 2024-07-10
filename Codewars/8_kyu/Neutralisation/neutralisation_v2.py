def neutralise(*s):
    return "".join(f"0{x}"[x==y]for x,y in zip(*s))
