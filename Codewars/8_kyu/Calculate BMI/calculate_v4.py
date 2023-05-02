def bmi(w,h):
    return ["Underweight","Normal","Overweight","Obese"][((n:=w/h**2)>18.5)+(n>25)+(n>30)]
