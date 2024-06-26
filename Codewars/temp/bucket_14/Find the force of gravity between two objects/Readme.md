Problem description at Codewars can be found
[here](https://www.codewars.com/kata/5b609ebc8f47bd595e000627/train/python).

-------------

Your job is to find the gravitational force between two spherical objects (obj1, obj2).

#### Input
Two arrays are given:
* `arr_val` (value array), consists of 3 elements
  * 1st element: mass of obj 1
  * 2nd element: mass of obj 2
  * 3rd element: distance between their centers
* `arr_unit` (unit array), consists of 3 elements
  * 1st element: unit for mass of obj 1
  * 2nd element: unit for mass of obj 2
  * 3rd element: unit for distance between their centers
<br>

mass units are:
* kilogram (kg)
* gram (g)
* milligram (mg)
* microgram (μg)
* pound (lb)
<br>

distance units are:
* meter (m)
* centimeter (cm)
* millimeter (mm)
* micrometer (μm)
* feet (ft)

#### Note
value of G = 6.67 × 10<sup>−11</sup>N $\cdot$ kg<sup>−2</sup> $\cdot$ m<sup>2</sup>
<br>

1 ft = 0.3048 m
<br>

1 lb = 0.453592 kg
<br>

return value must be Newton for force (obviously)
<br>

`μ` copy this from here to use it in your solution
