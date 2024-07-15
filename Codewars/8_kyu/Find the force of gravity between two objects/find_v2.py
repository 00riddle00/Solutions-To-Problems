def solution(v,u):
    m1,m2 = v[0] * (m:={"kg":1, "g":1e-3, "mg":1e-6, "μg":1e-9, "lb":0.453592})[u[0]], v[1] * m[u[1]]
    r = v[2] * {"m":1, "cm":1e-2, "mm":1e-3, "μm":1e-6, "ft":0.3048}[u[2]]
    return (G:=6.67e-11)*m1*m2 / r**2