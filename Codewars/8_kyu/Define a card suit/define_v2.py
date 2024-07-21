def define_suit(card):
    return {"C":"clubs","D":"diamonds","H":"hearts"}.get(card[-1],"spades")
