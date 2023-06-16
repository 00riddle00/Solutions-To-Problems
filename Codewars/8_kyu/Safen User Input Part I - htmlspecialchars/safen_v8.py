from re import sub

def html_special_chars(data):
    # if 2nd arg to .sub() is a function, it is called for every non-overlapping occurrence of pattern.
    # x is a Python RegEx Match Object
    # x[0] is the same as x.group(0) or x.group()
    return sub('[<>"&]', lambda x: {'<':'&lt;','>':'&gt;','"':'&quot;','&':'&amp;'}.get(x[0]),data)
