calculate_age=lambda b,y: f"You are {d} year{s} old." if ((s := f"{'s'*(abs(d:=y-b)>1)}") or 1) and d > 0 else f"You will be born in {-d} year{s}." if d < 0 else "You were born this very year!"
