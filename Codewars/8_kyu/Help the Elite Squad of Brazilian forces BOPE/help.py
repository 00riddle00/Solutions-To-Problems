import math

def mag_number(info):
    return math.ceil(3*info[1] / {"PT92":17, "M4A1":30, "M16A2":30, "PSG1":5}[info[0]])
