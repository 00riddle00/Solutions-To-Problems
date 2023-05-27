import re

def shortcut( s ):
    return re.sub('[aoeui]', '', s)
