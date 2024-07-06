def rain_amount(mm):
    return f"You need to give your plant {mm}mm of water" if (mm := max(0,40-mm)) else "Your plant has had more than enough water for today!"
