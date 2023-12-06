def multiple_of_index(arr):
    return [el for i,el in enumerate(arr) if i==el or i and el%i==0]
