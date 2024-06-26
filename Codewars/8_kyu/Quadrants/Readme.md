Problem description at Codewars can be found
[here](https://www.codewars.com/kata/643af0fa9fa6c406b47c5399/train/python).

-------------

#### Task
Given a point in a [Euclidean plane](https://en.wikipedia.org/wiki/Euclidean_plane) (`x` and `y`),
return the quadrant the point exists in: `1`, `2`, `3` or `4` (integer). `x` and `y` are non-zero
integers, therefore the given point never lies on the axes.

#### Examples
```
(1, 2)     => 1
(3, 5)     => 1
(-10, 100) => 2
(-1, -9)   => 3
(19, -56)  => 4
```

#### Reference
![Quadrants](images/Quadrants.png)

There are four quadrants:
1. First quadrant, the quadrant in the top-right, contains all points with positive X and Y
2. Second quadrant, the quadrant in the top-left, contains all points with negative X, but positive
   Y
3. Third quadrant, the quadrant in the bottom-left, contains all points with negative X and Y
4. Fourth quadrant, the quadrant in the bottom-right, contains all points with positive X, but
   negative Y
<br>

More on quadrants: [Quadrant (plane geometry) -
Wikipedia](https://en.wikipedia.org/wiki/Quadrant_(plane_geometry))
<br>

#### Task Series
1. Quadrants (this kata)
2. [Quadrants 2: Segments](https://www.codewars.com/kata/643ea1adef815316e5389d17/train/python)
