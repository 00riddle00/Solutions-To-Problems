Problem description at Codewars can be found
[here](https://www.codewars.com/kata/58e8cad9fd89ea0c6c000258/train/python).

-------------

A family of [kookaburras](https://en.wikipedia.org/wiki/Laughing_kookaburra) are in my backyard.
<br>

I can't see them all, but I can hear them!
<br>

#### How many kookaburras are there?
![Kookaburras](images/Kookaburras.png)

#### Hint
The trick to counting kookaburras is to listen carefully
* The males sound like `HaHaHa`...
* The females sound like `hahaha`...
* And they always alternate male/female
<br>

#### Examples
* `ha` = female => 1
* `Ha` = male => 1
* `Haha` = male + female => 2
* `haHa` = female + male => 2
* `hahahahaha` = female => 1
* `hahahahahaHaHaHa` = female + male => 2
* `HaHaHahahaHaHa` = male + female + male => 3
