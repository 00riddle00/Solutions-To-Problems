def first_non_consecutive(a,p=None):
    if not a:
        return None
    elif p is None or a[0]-p==1:
        return first_non_consecutive(a[1:],a[0])
    else:
        return a[0]
