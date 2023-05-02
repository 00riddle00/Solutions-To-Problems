def human_years_cat_years_dog_years(h):
    match h:
        case 1: return [1,15,15]
        case 2: return [2,24,24]
        case _:
            c = 24 + 4*(h-2)
            return [h, c, c+h-2]
