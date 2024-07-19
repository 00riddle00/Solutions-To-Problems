class Ghost: __init__=lambda s: setattr(s, "color", __import__("random").choice(("white","purple","yellow","red")))
