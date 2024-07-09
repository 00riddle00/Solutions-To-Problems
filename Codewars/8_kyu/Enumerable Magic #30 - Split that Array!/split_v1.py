def partition(arr, cond):
    return (f:=list(filter(cond,arr))), [x for x in arr if x not in f]
