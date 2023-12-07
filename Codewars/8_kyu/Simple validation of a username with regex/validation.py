import re

def validate_usr(username):
    return bool(re.match("[a-z\d_]{4,16}$", username))
