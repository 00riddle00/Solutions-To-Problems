def generate_link(u):
    return "http://www.codewars.com/users/" + "".join([x if x.isalnum() or x in "./_~" else f"%{ord(x):X}" for x in u])
