def cannons_ready(gunners):
    return ('Shiver me timbers!','Fire!')[all(map(lambda a: a=="aye", gunners.values()))]
