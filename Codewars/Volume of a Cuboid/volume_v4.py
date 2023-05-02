get_volume_of_cuboid = lambda *d: __import__("functools").reduce(__import__("operator").mul, d)
