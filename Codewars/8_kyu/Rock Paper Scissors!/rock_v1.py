def rps(p1, p2):
    return {**dict.fromkeys([0], "Draw!"), **dict.fromkeys([-1,-2,3], "Player 1 won!"), **dict.fromkeys([1,2,-3], "Player 2 won!")}[ord(p1[0]) - ord(p2[0])]
