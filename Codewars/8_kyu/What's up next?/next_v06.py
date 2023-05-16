next_item = lambda xs,item: (lambda x: next(x, None) if item in x else None)(iter(xs))
