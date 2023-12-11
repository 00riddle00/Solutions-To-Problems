import re

animals=lambda h,l: (((chicken:=2*h-l/2),(cows:=l/2-h)),"No solutions")[bool(re.search("-|\.[^0]", f"{chicken}{cows}"))]
