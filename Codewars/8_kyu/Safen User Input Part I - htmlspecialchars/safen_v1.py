def html_special_chars(data):
    return data.translate(dict(zip(map(ord, '<>"&'),(f"&{_};" for _ in ["lt","gt","quot","amp"]))))
