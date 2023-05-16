def next_item(xs, item):
    it = iter(xs)

    for x in it:
        if x == item:
            try: return next(it)
            except StopIteration: None
