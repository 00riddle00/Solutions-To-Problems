def multiple_of_index(arr):
    zeroth = [0] if arr[0] == 0 else []
    return zeroth + [arr[1]] + [el for i, el in enumerate(arr[2:],2) if el % i == 0]
