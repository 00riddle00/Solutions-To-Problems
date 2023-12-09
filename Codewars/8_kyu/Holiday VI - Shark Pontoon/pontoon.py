def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    return ["Shark Bait!", "Alive!"][pontoon_distance / you_speed < shark_distance*(1+dolphin) / shark_speed]
