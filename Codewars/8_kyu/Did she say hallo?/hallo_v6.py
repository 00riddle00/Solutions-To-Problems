import re

def validate_hello(msg):
    return len(re.findall("h[ae]llo|ciao|salut|hola|ahoj|czesc", msg, re.I))>0
