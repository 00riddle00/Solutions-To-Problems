g = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(b):
    return [*filter(lambda x: x not in g, b)]
