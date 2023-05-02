def feast(beast, dish):
    return dish.startswith(beast[0]) & dish.endswith(beast[-1])
