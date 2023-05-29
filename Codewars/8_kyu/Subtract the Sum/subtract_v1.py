def subtract_sum(n):
    return (n := n - sum(int(c) for c in str(n))) <= 100 and fruit(n) or subtract_sum(n)

def fruit(n):
    if n % 9 == 0:
        return 'apple'
    elif n in [4,6,25,29,48,50,71,73,92,94,96]:
        return 'banana'
    elif n in  [20,22,41,43,62,64,66,85,87,89]:
        return 'cherry'
    elif n in  [11,13,34,55,57,59,78,80]:
        return 'cucumber'
    elif n in  [15,17,19,38,40,61,82,84,86]:
        return 'grape'
    elif n in  [1,3,24,26,47,49,68,70,91,93]:
        return 'kiwi'
    elif n in  [5,7,28,30,32,51,53,74,76,95,97]:
        return 'melon'
    elif n in  [14,16,35,37,39,58,60,83]:
        return 'orange'
    elif n in  [2,21,23,42,44,46,65,67,69,88]:
        return 'pear'
    elif n in  [8,10,12,31,33,52,56,75,77,79,98,100]:
        return 'pineapple'
