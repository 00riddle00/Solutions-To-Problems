def ensure_question(s):
    return re.sub("(?:(?<=^)|(?<=[^?]))$", "?", s)
