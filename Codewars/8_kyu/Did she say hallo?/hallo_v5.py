import re

def validate_hello(msg):
    return bool(re.match("(?i).*(h[ea]llo|ciao|salut|hola|ahoj|czesc)", msg))
