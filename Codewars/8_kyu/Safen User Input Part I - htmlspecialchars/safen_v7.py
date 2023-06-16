from html import escape

def html_special_chars(data):
    return "'".join(map(escape, data.split("'")))
