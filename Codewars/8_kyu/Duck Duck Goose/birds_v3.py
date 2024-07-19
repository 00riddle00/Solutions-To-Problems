def duck_duck_goose(players, goose):
    return players[~-goose % len(players)].name
