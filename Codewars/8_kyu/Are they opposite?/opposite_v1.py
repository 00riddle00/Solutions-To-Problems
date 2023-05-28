def is_opposite(s1,s2):
    return all((abs(ord(s1[i])-ord(s2[i]))==32 for i in range(len(s1)))) if s1 else False
