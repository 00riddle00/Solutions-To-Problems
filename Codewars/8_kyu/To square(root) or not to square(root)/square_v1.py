import math

def square_or_square_root(arr):
    return [x**2 if sqrt % 1 else sqrt for x in arr if (sqrt := math.sqrt(x))]
