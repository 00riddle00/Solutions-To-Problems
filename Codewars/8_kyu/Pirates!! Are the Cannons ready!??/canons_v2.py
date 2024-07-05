def cannons_ready(gunners):
    return ("Shiver me timbers!","Fire!")[all(map("aye".__eq__, gunners.values()))]
