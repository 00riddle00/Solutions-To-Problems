def first_non_consecutive(a):
    return next((a[i+1] for i in range(len(a)-1) if a[i+1]-a[i]-1),None)
