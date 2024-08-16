Problem description at Codewars can be found
[here](https://www.codewars.com/kata/636f26f52aae8fcf3fa35819/train/python).

-------------

If I were to ask you the size of `"hello"`, what would you say?
<br>

Wait, let me rephrase the question:
<br>

If I were to ask you the total byte size of `"hello"`, how many bytes do you think it takes up?
<br>

I'll give you a hint: it's not 5.
```
len("hello")  -->  5

byte size -->  54
```
<br>

54? What?!
<br>

Here's why: every string has to have an encoding (e.g ASCII),the info that makes it an `object`, as
well as all of it's other properites... it would have to take up a bit more than 5 bytes, wouldn't
it?
<br>

This might be useful for sending something over a network, where you need to represent the memory
size the item takes up.

#### Task
In this kata, you need to return the number of bytes (aka. memory size) a given object takes up.
<br>

Different variable types will be given, but they will all be valid. Also, random generation for
strings takes out of Unicode, not the regular 255 ascii letters.
<br>

P.S: Don't be afraid to use the internet. It "byte" come in handy :)

#### Other Examples
```
Object    Bytes    Why?
----      ----     ---- 
"龘"       76      Other character sets take up more room.
123        28      Numbers don't have as much info in them. 
[1,2]      72      Lists have more info stored (e.g index).
(1,2)      56      Tuples are (kind of) just bowls of data.
```
