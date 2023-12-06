def multiple_of_index(arr):
    return [el for i,el in enumerate(arr) if (i==0 and el==0) or (i!=0 and el%i==0)]
