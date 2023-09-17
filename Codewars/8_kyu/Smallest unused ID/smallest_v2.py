def next_id(arr):
    return next(id for id in range(max(arr, default=0)+2) if id not in arr)
