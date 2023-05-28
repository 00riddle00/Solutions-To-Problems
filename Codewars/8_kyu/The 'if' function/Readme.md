Problem description at Codewars can be found
[here](https://www.codewars.com/kata/54147087d5c2ebe4f1000805/train/python).

-------------

Create a function called `_if` which takes 3 arguments: a value `bool` and 2 functions (which do not
take any parameters): `func1` and `func2`
<br>

When `bool` is truthy, `func1` should be called, otherwise call the `func2`.
<br>

Example:
```
def truthy(): 
  print("True")
  
def falsey(): 
  print("False")
  
_if(True, truthy, falsey)
# prints 'True' to the console
```
