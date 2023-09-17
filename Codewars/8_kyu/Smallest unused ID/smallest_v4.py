next_id=lambda arr: __import__("functools").reduce(lambda acc, x: acc + 1 if acc == x else acc, sorted(arr), 0)
