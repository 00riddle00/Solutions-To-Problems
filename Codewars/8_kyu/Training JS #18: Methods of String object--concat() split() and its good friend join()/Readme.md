Problem description at Codewars can be found
[here](https://www.codewars.com/kata/57280481e8118511f7000ffa/train/python).

-------------

Implement a function which accepts 2 arguments: `string` and `separator`.
<br>

The expected algorithm: split the `string` into words by spaces, split each word into separate
characters and join them back with the specified `separator`, join all the resulting "words" back
into a sentence with spaces.
<br>

For example:
```
splitAndMerge("My name is John", " ")  ==  "M y n a m e i s J o h n"
splitAndMerge("My name is John", "-")  ==  "M-y n-a-m-e i-s J-o-h-n"
splitAndMerge("Hello World!", ".")     ==  "H.e.l.l.o W.o.r.l.d.!"
splitAndMerge("Hello World!", ",")     ==  "H,e,l,l,o W,o,r,l,d,!"
```
