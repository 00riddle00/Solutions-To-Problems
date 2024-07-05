import unicodedata

def switch_it_up(n):
    return unicodedata.name(f"{n}").split()[1].title()
