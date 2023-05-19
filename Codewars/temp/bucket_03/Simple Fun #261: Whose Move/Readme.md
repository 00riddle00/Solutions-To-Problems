Problem description at Codewars can be found
[here](https://www.codewars.com/kata/59126992f9f87fd31600009b/train/python).

-------------

#### Task
Two players - `"black"` and `"white"` are playing a game. The game consists of several rounds. If a
player wins in a round, he is to move again during the next round. If a player loses a round, it's
the other player who moves on the next round. Given whose turn it was on the previous round and
whether he won, determine whose turn it is on the next round.

#### Input/Output
`[input]` string `lastPlayer/`$last_player`
<br>

`"black"` or `"white"` - whose move it was during the previous round.
<br>

`[input]` boolean `win`/`$win` 
<br>

`true` if the player who made a move during the previous round won, `false` otherwise.
<br>

`[output]` a string
<br>

Return `"white"` if white is to move on the next round, and `"black"` otherwise.

#### Example
For `lastPlayer = "black" and win = false`, the output should be `"white"`.
<br>

For `lastPlayer = "white" and win = true`, the output should be `"white"`.
<br>
