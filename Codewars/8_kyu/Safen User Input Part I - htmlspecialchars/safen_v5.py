def html_special_chars(data):
    return data.replace('&', "&amp;").replace('>', "&gt;").replace('<', "&lt;").replace('\"', "&quot;")
