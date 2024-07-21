def count_squares(x):
    """
    Number of cuts = x
    The total number of cubes = (x+1)^3
    The number of all cubes with no paint on = (x-1)^3
   
    Number of cubes with paint on at least one side:
    (x+1)^3 - (x-1)^3 =
    = (x+1)(x+1)(x+1) - (x-1)(x-1)(x-1) =
    = x^3 + 3x^2 + 3x + 1 - (x^3 - 3x^2 + 3x - 1) =
    = 6x^2 + 2
    """
    return 6 * x**2 + 2
