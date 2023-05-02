def first_non_consecutive(a):
    return next((x for i,x in enumerate(a,a[0]) if x-i),None)
