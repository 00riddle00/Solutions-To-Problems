def grader(s):
    return "ABCD"[int(10*(0.99-s))] if 0.6 <= s <= 1 else "F"
