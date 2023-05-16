def cookie(x):
    return f"Who ate the last cookie? It was {('the dog', 'Zach', 'Monica')[(type(x)==str) + 2*(type(x) in (int,float))]}!"
