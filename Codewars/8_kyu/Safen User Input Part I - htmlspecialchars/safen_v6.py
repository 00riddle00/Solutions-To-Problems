from html import escape

def html_special_chars(data):
    return escape(data).replace("&#x27;","'")
