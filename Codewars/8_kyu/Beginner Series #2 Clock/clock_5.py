from datetime import timedelta

def past(h, m, s):
    return 1e3 * timedelta(hours=h, minutes=m, seconds=s).total_seconds()
