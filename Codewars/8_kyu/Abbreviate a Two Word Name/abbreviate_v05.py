def abbrevName(n):
    return (l := n.upper().split()) and f'{l[0][0]}.{l[1][0]}'
