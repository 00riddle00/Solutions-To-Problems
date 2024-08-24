def to_csv_text(arr):
    return "\n".join(",".join(str(x) for x in row) for row in arr)
