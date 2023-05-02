bmi = lambda w,h: ("Obese", "Overweight", "Normal", "Underweight")[((n := w/h**2) <= 30) + (n <= 25) + (n <= 18.5)]
