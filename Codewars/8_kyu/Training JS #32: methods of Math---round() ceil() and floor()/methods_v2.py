round_it=lambda n: round(n+0.5*(((i:=str(n).index(".")-len(str(n))/2+0.5)<0)-(i>0)))
