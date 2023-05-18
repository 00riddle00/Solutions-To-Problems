Problem description at Codewars can be found
[here](https://www.codewars.com/kata/58fd9f6213b00172ce0000c9/train/python).

-------------

#### Task
You are given a decimal number `n` as a string. Transform it into an array of numbers (given as
strings again), such that each number has only one nonzero digit and their sum equals n.
<br>

Each number in the output array should be written without any leading and trailing zeros.
<br>

#### Input/Output
- `[input]` string `n`
<br>

A non-negative number.
<br>

`1 ≤ n.length ≤ 30.`
<br>

* `[output]` a string array
<br>

Elements in the array should be sorted in descending order.
<br>

#### Example
For `n = "7970521.5544"` the output should be:
```
["7000000", 
"900000", 
"70000", 
"500", 
"20", 
"1", 
".5",
".05",
".004",
".0004"]
```
<br>

For `n = "7496314"`, the output should be:
```
["7000000", 
"400000", 
"90000", 
"6000", 
"300", 
"10", 
"4"]
```
<br>

For `n = "0"`, the output should be `[]`
