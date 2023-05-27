Problem description at Codewars can be found
[here](https://www.codewars.com/kata/5732d3c9791aafb0e4001236/train/python).

-------------

Coding in function `roundIt`. function accept 1 parameter `n`. It's a number with a decimal point.
Please use different methods based on the location of the decimal point, turn the number into an
integer.
<br>

If the decimal point is on the left side of the number (that is, the count of digits on the left of
the decimal point is less than that on the right), Using `ceil()` method.
```
roundIt(3.45) should return 4
```
<br>

If the decimal point is on the right side of the number (that is, the count of digits on the left of
the decimal point is more than that on the right), Using `floor()` method.
```
roundIt(34.5) should return 34
```
<br>

If the decimal point is on the middle of the number (that is, the count of digits on the left of the
decimal point is equals that on the right), Using `round()` method.
```
roundIt(34.56) should return 35
```
