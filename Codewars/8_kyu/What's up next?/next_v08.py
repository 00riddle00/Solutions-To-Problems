def next_item(xs, item):
    if item in (it := iter(xs)): return next(it, None)
