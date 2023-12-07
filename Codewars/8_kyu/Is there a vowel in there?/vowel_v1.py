def is_vow(inp):
    return [chr(x) if chr(x) in "aeiou" else x for x in inp]
