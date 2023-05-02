get_grade=lambda *s: "ABCDF"[((m:=sum(s)/30)<9)+(m<8)+(m<7)+(m<6)]
