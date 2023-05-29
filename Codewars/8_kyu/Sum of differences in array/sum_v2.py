def sum_of_differences(arr):
    return arr[-1]-arr[0] if len(arr:=sorted(arr)) > 1 else 0
