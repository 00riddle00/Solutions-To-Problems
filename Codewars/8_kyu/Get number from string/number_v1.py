def get_number_from_string(s):
    return int("".join(filter(str.isdigit, s)))
