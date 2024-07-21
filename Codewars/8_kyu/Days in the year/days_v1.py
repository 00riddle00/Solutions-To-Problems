def year_days(y):
    return f"{y} has {365+(not y%400 or y%100 and not y%4)} days"
