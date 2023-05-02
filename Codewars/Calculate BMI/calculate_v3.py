def bmi(w,h):
    return ("Obese","Overweight","Normal","Underweight")[((n:=w/h**2)<30)+(n<25)+(n<18.5)]
