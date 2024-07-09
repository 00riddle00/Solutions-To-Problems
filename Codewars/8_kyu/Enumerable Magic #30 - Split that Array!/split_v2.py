def partition(arr, cond):
    return ([x for x in arr if cond(x)],[x for x in arr if not cond(x)])
