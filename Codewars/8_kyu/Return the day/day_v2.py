def whatday(num):
    return ["Wrong, please enter a number between 1 and 7",["","Sun","Mon","Tues","Wednes","Thurs","Fri","Satur"][num%8]+"day"][0<num<8]
