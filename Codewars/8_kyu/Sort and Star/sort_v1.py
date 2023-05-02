def two_sort(array):
    return '***'.join(([(cs := array[0])] + [(cs := s) for s in array[1:] if (s[0] < cs[0] or s[0] == cs[0] and s[1] < cs[1])])[-1])
