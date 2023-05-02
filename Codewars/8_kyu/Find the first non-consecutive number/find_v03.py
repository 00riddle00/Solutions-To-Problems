def first_non_consecutive(a):
    for i in range(len(a)-1):
        if a[i+1]-a[i]-1:
            return a[i+1]
