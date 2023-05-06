Problem description at Codewars can be found
[here](https://www.codewars.com/kata/58afce23b0e8046a960000eb/train/python).

-------------

#### Task
An `ATM` ran out of 10 dollar bills and only has `100, 50 and 20` dollar bills.
<br>

Given an amount between `40 and 10000 dollars (inclusive)` and assuming that the ATM wants to use as
few bills as possible, determinate the minimal number of 100, 50 and 20 dollar bills the ATM needs
to dispense (in that order).
<br>

#### Example
For `n = 250`, the result should be `[2, 1, 0]`.
<br>

For `n = 260`, the result should be `[2, 0, 3]`.
<br>

For `n = 370`, the result should be `[3, 1, 1]`.
<br>

#### Input/Output
- `[input]` integer `n` Amount of money to withdraw. Assume that `n` is always exchangeable with
  `[100, 50, 20]` bills.
- `[output]` integer array An array of number of `100, 50 and 20` dollar bills needed to complete
  the withdraw (in that order).
