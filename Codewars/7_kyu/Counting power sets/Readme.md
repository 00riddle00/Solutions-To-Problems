Problem description at Codewars can be found
[here](https://www.codewars.com/kata/54381f0b6f032f933c000108/train/python).

-------------

In this kata, you must create a function `powers`/`Powers` that takes an array, and returns the
number of subsets possible to create from that list. In other words, counts the power sets.
<br>

For instance
```
powers([1,2,3]) => 8
```
<br>

...due to...
<br>

```
powers([1,2,3]) =>
[[],
 [1],
 [2],
 [3],
 [1,2],
 [2,3],
 [1,3],
 [1,2,3]]
```
<br>

Your function should be able to count sets up to the size of 500, so watch out; pretty big numbers
occur there!
<br>

For comparison, my Haskell solution can compute the number of sets for an array of length 90 000 in
less than a second, so be quick!
<br>

You should treat each array passed as a set of unique values for this kata.

#### Examples:
```
powers([])        => 1
powers([1])       => 2
powers([1,2])     => 4
powers([1,2,3,4]) => 16
```
<br>

Inspired by [this kata](https://www.codewars.com/kata/by-the-power-set-of-castle-grayskull) by
[xcuthulu](https://www.codewars.com/users/xcthulhu) - refer to it if you're stuck!
