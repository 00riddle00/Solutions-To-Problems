def first_non_consecutive(a):
    return next((x for i,x in enumerate(a) if x-a[0]-i),None)
