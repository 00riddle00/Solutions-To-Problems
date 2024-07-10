import re

def validate_hello(msg):
    return bool(re.search("h[ae]llo|ciao|salut|hola|ahoj|czesc", msg, re.I))
