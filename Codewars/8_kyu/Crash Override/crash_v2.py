alias_gen=lambda f,l: FIRST_NAME[f]+" "+SURNAME[l] if ((f:=f[0].upper())+(l:=l[0].upper())).isalpha() else "Your name must start with a letter from A - Z."
