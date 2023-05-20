Problem description at Codewars can be found
[here](https://www.codewars.com/kata/574b3b1599d8f897470018f6/train/python).

-------------

Americans are odd people: in their buildings, the first floor is actually the ground floor and there
is no 13th floor (due to superstition).
<br>

Write a function that given a floor in the american system returns the floor in the european system.
<br>

With the 1st floor being replaced by the ground floor and the 13th floor being removed, the numbers
move down to take their place. In case of above 13, they move down by two because there are two
omitted numbers below them.
<br>

Basements (negatives) stay the same as the universal level.
<br>

[More information here](https://en.wikipedia.org/wiki/Storey#European_scheme)

#### Examples
```
1  =>  0 
0  =>  0
5  =>  4
15  =>  13
-3  =>  -3
```
