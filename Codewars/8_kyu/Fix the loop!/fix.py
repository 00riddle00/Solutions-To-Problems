def list_animals(animals):
    return  "".join(f"{i+1}. {x}\n" for i,x in enumerate(animals))
