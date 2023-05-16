def calculator(x,y,op):
    return eval(f"x {op} y") if str(op) in "+-*/" and (str(x)+str(y)).isdigit() else "unknown value"
