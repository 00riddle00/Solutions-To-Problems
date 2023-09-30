def cannons_ready(gunners):
    return ('Shiver me timbers!','Fire!')[set(gunners.values())=={'aye'}]
