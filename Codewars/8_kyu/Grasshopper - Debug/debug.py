def weather_info (temp):
    return f"{(c := (temp - 32) * (5/9))} is{' above' if c >= 0 else ''} freezing temperature"
