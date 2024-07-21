def define_suit(card):
    return "hearts clubs diamonds ace of spades".split()[ord(card[-1])%6]
