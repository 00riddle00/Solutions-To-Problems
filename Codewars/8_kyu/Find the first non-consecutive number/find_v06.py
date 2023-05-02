def first_non_consecutive(a):
    return next((j for i,j in zip(a,a[1:]) if j-i-1),None)
