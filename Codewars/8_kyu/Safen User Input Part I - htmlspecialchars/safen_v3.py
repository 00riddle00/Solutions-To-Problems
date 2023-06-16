def html_special_chars(data):
    return data.translate(str.maketrans({'<':'&lt;', '>':'&gt;', '"':'&quot;', '&':'&amp;'}))
