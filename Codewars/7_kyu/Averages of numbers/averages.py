def averages(arr):
    return [*map(lambda x, y: (x + y) /2, arr, arr[1:])] if arr else []
