def count_positives_sum_negatives(arr):
    return arr and [len([*filter(0..__lt__,arr)]), sum(filter(0..__gt__,arr))] or []
