Problem description at Codewars can be found
[here](https://www.codewars.com/kata/574b1916a3ebd6e4fa0012e7/train/python).

-------------

The full name of this kata:
<br>

"They say that only the name is long enough to attract attention. They also said that only a simple
Kata will have someone to solve it. This is a sadly story #1: Are they opposite?"
<br>

#### Task
Give you two strings: `s1` and `s2`. If they are opposite, return `true`; otherwise, return `false`.
Note: The result should be a boolean value, instead of a string.
<br>

The `opposite` means: All letters of the two strings are the same, but the case is opposite. you can
assume that the string only contains letters or it's a empty string. Also take note of the edge case
- if both strings are empty then you should return `false`/`False`.

#### Examples (input -> output)
```
"ab","AB"     -> true
"aB","Ab"     -> true
"aBcd","AbCD" -> true
"AB","Ab"     -> false
"",""         -> false
```
