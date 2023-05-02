def quarter_of(month):
    p,q = divmod(month,3)
    return p + (q>0)
