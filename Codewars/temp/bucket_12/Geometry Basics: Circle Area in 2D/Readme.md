Problem description at Codewars can be found
[here](https://www.codewars.com/kata/58e3f824a33b52c1dc0001c0/train/python).

-------------

This series of katas will introduce you to basics of doing geometry with computers.
<br>

Write the function `circleArea`/`CircleArea` which takes in a `Circle` object and calculates the
area of that circle.

The `Circle` class can be seen below:
```
// Represents a Circle where center is a Point and radius is a Number
class Circle {
  constructor(center, radius) { 
    this.center = center; 
    this.radius = radius;
  }
}
```
<br>

And the `Point` class can be seen below:
```
// Represents a Point where x and y are Numbers
class Point {
  constructor (x,y) { 
    this.x = x;
    this.y = y; 
  }
}
```
<br>

Tests round answers to 6 decimal places.
