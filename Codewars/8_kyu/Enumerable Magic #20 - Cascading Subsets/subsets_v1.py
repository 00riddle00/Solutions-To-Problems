def each_cons(lst, n):
    return [lst[i:][:n] for i in range(len(lst)) if len(lst[i:]) >= n]
