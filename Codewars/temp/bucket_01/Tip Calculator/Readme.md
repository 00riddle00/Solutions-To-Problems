Problem description at Codewars can be found
[here](https://www.codewars.com/kata/56598d8076ee7a0759000087/train/python).

-------------

Complete the function, which calculates how much you need to tip based on the total amount of the
bill and the service.
<br>

You need to consider the following ratings:
* Terrible: tip 0%
* Poor: tip 5%
* Good: tip 10%
* Great: tip 15%
* Excellent: tip 20%
<br>

The rating is case insensitive (so "great" = "GREAT"). If an unrecognised rating is received, then
you need to return:

* `"Rating not recognised"` in Javascript, Python and Ruby...
* ...or `null` in Java
* ...or `-1` in C#
<br>

Because you're a nice person, you always round up the tip, regardless of the service.
