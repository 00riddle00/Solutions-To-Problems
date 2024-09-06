HQ9 = lambda c: [
    None,
    "Hello World!",
    "Q",
    (b1 := f"1 {(bt:='bottle')} {(o:='of beer')}")
    and "".join(
        [
            f"{n} {(b:=f'{bt}s {o}')} {(w:='on the wall')}, {n} {b}.\n"
            + f"{(t:='Take one down and pass it around')}, {n-1} {b} {w}.\n"
            for n in range(99, 2, -1)
        ]
        + [
            f"2 {b} {w}, 2 {b}.\n{t}, {b1} {w}.\n"
            f"{b1} {w}, {b1}.\n{t}, no {(m:='more')} {b} {w}.\n"
            f"No {m} {b} {w}, no {m} {b}.\nGo to the store and buy some {m}, 99 {b} {w}."
        ]
    ),
][(c == "H") + 2 * (c == "Q") + 3 * (c == "9")]
