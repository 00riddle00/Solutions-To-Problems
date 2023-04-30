def count_positives_sum_negatives(arr):
    np = [x for x in arr if x <= 0]
    return arr and [len(arr)-len(np),sum(np)] or []
