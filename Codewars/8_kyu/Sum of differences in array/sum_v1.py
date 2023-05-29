def sum_of_differences(arr):
    return arr[0]-arr[-1] if len(arr := sorted(arr,reverse=1)) > 1 else 0
