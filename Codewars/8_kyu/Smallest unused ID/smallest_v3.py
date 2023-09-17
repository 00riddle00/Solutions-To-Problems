def next_id(arr):
    return next(id for id in range(max([0]+arr)+2) if id not in arr)
