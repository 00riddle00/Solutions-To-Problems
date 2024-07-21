from calendar import isleap

def year_days(y):
    return f"{y} has {365+isleap(y)} days"
