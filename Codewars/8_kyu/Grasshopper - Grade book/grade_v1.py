def get_grade(s1, s2, s3):
    offset = int(9.5 - (s1 + s2 + s3) // 30)
    return chr(65 + offset) if offset < 4 else "F"
