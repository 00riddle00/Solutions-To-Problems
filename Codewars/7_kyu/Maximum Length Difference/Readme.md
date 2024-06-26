Problem description at Codewars can be found
[here](https://www.codewars.com/kata/5663f5305102699bad000056/train/python).

-------------

You are given two arrays `a1` and `a2` of strings. Each string is composed with letters from `a` to
`z`. Let `x` be any string in the first array and `y` be any string in the second array.
<br>

`Find max(abs(length(x) − length(y)))`
<br>

If `a1` and/or `a2` are empty return `-1` in each language except in Haskell (F#) where you will
return `Nothing` (None).
<br>

#### Example:
```
a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(a1, a2) --> 13
```
<br>

#### Bash note:
* input : 2 strings with substrings separated by `,`
* output: number as a string
