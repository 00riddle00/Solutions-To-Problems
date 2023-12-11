animals = lambda h,l: ((h-(cows:=l/2-h),cows),"No solutions")[cows>h or cows<0 or l%2]
