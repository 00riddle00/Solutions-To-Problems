Problem description at Codewars can be found
[here](https://www.codewars.com/kata/5d59576768ba810001f1f8d6/train/python).

-------------

In this Kata you are expected to find the coefficients of quadratic equation of the given two roots
(`x1` and `x2`).
<br>

Equation will be the form of `ax^2 + bx + c = 0`
<br>

Return type is a Vector (tuple in Rust, Array in Ruby) containing coefficients of the equations in
the order `(a, b, c)`.
<br>

Since there are infinitely many solutions to this problem, we fix `a = 1`.
<br>

Remember, the roots can be written like `(x-x1) * (x-x2) = 0`

#### Example 1
```
quadratic(1,2) = (1, -3, 2)
```
<br>

This means `(x-1) * (x-2) = 0`; when we do the multiplication this becomes `x^2 - 3x + 2 = 0`

#### Example 2
```
quadratic(0,1) = (1, -1, 0)
```
<br>

This means `(x-0) * (x-1) = 0`; when we do the multiplication this becomes `x^2 - x + 0 = 0`

#### Notes
* Inputs will be integers.
* When `x1 == x2`, this means the root has the multiplicity of two
