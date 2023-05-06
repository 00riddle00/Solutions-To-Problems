Problem description at Codewars can be found
[here](https://www.codewars.com/kata/590bdaa251ab8267b800005b/train/python).

-------------

#### Task
Consider an array of integers `a`. Let `min(a)` be its minimal element, and let `avg(a)` be its
mean.
<br>

Define the center of the array `a` as array `b` such that:
```
- b is formed from a by erasing some of its elements.
- For each i, |b[i] - avg(a)| < min(a).
- b has the maximum number of elements among all the arrays
  satisfying the above requirements.
```
<br>

Given an array of integers, return its center.
<br>

#### Input/Output
`[input]` integer array `a`
<br>

Unsorted non-empty array of integers.
<br>

`2 ≤ a.length ≤ 50`,
<br>

`1 ≤ a[i] ≤ 350`.
<br>

`[output]` an integer array
<br>

#### Example
For `a = [8, 3, 4, 5, 2, 8]`, the output should be `[4, 5]`.
<br>

Here `min(a) = 2, avg(a) = 5`.
<br>

For `a = [1, 3, 2, 1]`, the output should be `[1, 2, 1]`.
<br>

Here `min(a) = 1, avg(a) = 1.75`.
