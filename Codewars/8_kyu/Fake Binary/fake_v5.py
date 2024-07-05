def fake_bin(s):
    return s.translate(s.maketrans("0123456789", "0"*5+"1"*5))
