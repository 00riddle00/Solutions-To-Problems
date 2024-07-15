import re

def sp_eng(sentence):
     return bool(re.search("english",sentence,re.I))
