def html_special_chars(data):
    return data.translate({60: "&lt;", 62: "&gt;", 34: "&quot;", 38: "&amp;"})
