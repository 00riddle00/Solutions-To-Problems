def rain_amount(mm):
    if (mm := max(0, 40 - mm)):
         return "You need to give your plant " + f"{mm}" + "mm of water"
    return "Your plant has had more than enough water for today!"
