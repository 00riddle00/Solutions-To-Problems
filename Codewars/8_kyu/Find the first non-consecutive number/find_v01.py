def first_non_consecutive(arr):
    return next(filter(lambda xy: abs(xy[0] - xy[1]) != 1, zip(arr, arr[1:])), [None])[-1]
