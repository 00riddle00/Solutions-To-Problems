def fake_bin(seq):
    return "".join("10"[x<"5"] for x in seq)
