def to_csv_text(arr):
    return "\n".join(",".join(map(str,row)) for row in arr)
