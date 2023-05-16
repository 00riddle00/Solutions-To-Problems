def next_item(xs, item):
    it = iter(xs)
    item in it
    return next(it, None)
