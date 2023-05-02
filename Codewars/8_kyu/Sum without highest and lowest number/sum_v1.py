def sum_array(arr):
    if not arr or len(arr) < 3: return 0
    sum = min = max = arr[0]
    for x in arr[1:]:
        if x < min:
            min = x
        elif x > max:
            max = x
        sum += x
    return sum - min - max
