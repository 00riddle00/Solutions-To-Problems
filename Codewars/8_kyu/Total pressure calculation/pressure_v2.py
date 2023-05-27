def solution(M1, M2, m1, m2, V, Tc):
    return ( (m1/M1 + m2/M2) * (R:=0.082) * (Tk := Tc + 273.15) ) / V
