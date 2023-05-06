Problem description at Codewars can be found
[here](https://www.codewars.com/kata/54fb963d3fe32351f2000102/train/python).

-------------

The Collatz Conjecture states that for any positive natural number `n`, this process:
- if `n` is even, divide it by `2`
- if `n` is odd, multiply it by `3` and add `1`
- repeat
<br>

will eventually reach `n = 1`.
<br>

For example, if `n = 20`, the resulting sequence will be:
```
[ 20, 10, 5, 16, 8, 4, 2, 1 ]
```
<br>

Write a program that will output the length of the Collatz Conjecture for any given `n`.

In the example above, the output would be `8`.
<br>

For more reading see: [Collatz Conjecture](http://en.wikipedia.org/wiki/Collatz_conjecture)
