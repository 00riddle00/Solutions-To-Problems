from html import escape

def html_special_chars(data, y="'"):
    return escape(data).replace(escape(y), y)
