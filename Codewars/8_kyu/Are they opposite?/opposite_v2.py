def is_opposite(x,y):
    return len(set(map(len,map(set,zip(x,y)))))==1
