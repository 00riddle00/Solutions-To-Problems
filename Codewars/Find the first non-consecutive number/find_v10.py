def first_non_consecutive(a):
    return next((x for x in a[1:] if x-1 not in a),None)
