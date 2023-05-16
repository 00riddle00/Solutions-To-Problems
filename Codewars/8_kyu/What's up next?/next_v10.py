next_item = lambda xs, item: next(it, None) if item in (it := iter(xs)) else None
