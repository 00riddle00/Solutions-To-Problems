Problem description at Codewars can be found
[here](https://www.codewars.com/kata/5596f6e9529e9ab6fb000014/train/python).

-------------

Write a function that receives two strings and returns n, where n is equal to the number of
characters we should shift the first string forward to match the second. The check should be case
sensitive.
<br>

For instance, take the strings "fatigue" and "tiguefa". In this case, the first string has been
rotated 5 characters forward to produce the second string, so 5 would be returned.
<br>

If the second string isn't a valid rotation of the first string, the method returns -1.
<br>

#### Examples:
```
"coffee", "eecoff" => 2
"eecoff", "coffee" => 4
"moose", "Moose" => -1
"isn't", "'tisn" => 2
"Esham", "Esham" => 0
"dog", "god" => -1
```
