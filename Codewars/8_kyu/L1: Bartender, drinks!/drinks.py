def get_drink_by_profession(param):
    match param.lower():
        case "jabroni":          return "Patron Tequila"
        case "school counselor": return "Anything with Alcohol"
        case "programmer":       return "Hipster Craft Beer"
        case "bike gang member": return "Moonshine"
        case "politician":       return "Your tax dollars"
        case "rapper":           return "Cristal"
    return "Beer"
