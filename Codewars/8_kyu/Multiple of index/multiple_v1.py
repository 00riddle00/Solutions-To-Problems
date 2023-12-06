def multiple_of_index(arr):
    zeroth = [0] if arr[0] == 0 else []
    return zeroth + [el for i, el in enumerate(arr[1:],1) if el % i == 0]
