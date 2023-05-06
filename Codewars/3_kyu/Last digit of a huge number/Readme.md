Problem description at Codewars can be found
[here](https://www.codewars.com/kata/5518a860a73e708c0a000027/train/python).

-------------

For a given list `[x1, x2, x3, ..., xn]` compute the last (decimal) digit of `x1 ^ (x2 ^ (x3 ^ (... ^ xn)))`.
<br>

E. g., with the input `[3, 4, 2]`, your code should return `1` because `3 ^ (4 ^ 2) = 3 ^ 16 = 43046721`.
<br>

Beware: powers grow incredibly fast. For example, `9 ^ (9 ^ 9)` has more than 369 millions of
digits. `lastDigit` has to deal with such numbers efficiently.
<br>

Corner cases: we assume that `0 ^ 0 = 1` and that `lastDigit` of an empty list equals to 1.
<br>

This kata generalizes [Last digit of a large
number](https://www.codewars.com/kata/last-digit-of-a-large-number/haskell); you may find useful to
solve it beforehand.
