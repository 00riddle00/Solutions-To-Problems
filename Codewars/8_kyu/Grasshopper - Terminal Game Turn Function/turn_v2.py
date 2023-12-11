def do_turn():
    return [_() for _ in (roll_dice, move, combat, get_coins, buy_health, print_status)]
