def to_csv_text(arr):
    return str(arr)[2:-2].replace("], [","\n").replace(" ","");
