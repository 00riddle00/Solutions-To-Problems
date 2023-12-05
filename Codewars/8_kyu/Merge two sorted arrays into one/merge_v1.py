def merge_arrays(arr1, arr2):
    return [*(dict.fromkeys(sorted(arr1 + arr2)))]
