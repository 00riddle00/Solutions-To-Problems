import re

def validate_hello(msg):
    return bool(re.search("hello|ciao|salut|hallo|hola|ahoj|czesc", msg, re.I))
