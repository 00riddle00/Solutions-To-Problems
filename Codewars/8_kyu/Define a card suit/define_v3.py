import re

def define_suit(card):
    return re.search(rf"\b{card[-1]}\w+", "clubs diamonds hearts spades", re.I)[0]
