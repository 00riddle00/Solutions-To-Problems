def first_non_consecutive(a):
    return next((x for x in a[1:] if a.count(x-1)==0),None)
