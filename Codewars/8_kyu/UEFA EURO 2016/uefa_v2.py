def uefa_euro_2016(t,s):
    return f"At match {t[0]} - {t[1]}, {[t[s[0]<s[1]]+' won!','teams played draw.'][s[0]==s[1]]}"
