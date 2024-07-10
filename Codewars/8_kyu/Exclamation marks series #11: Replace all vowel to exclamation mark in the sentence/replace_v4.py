def replace_exclamation(s):
    return [(s:=s.replace(i,"!")) for i in "aeiouAEIOU"][-1]
