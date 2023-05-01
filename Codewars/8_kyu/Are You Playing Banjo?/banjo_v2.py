def are_you_playing_banjo(n):
    return f"{n} {('does not play','plays')[n[0] in 'rR']} banjo"
