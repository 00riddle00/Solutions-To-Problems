Problem description at Codewars can be found
[here](https://www.codewars.com/kata/574c5075d27783851800169e/train/python).

-------------

#### Description
Everybody has probably heard of the animal heads and legs problem from the earlier years at school.
It goes:
<br>

`“A farm contains chickens and cows. There are x heads and y legs. How many chickens and cows are
there?”`
<br>

Where x <= 1000 and y <=1000

#### Task
Assuming there are no other types of animals, work out how many of each animal are there.
<br>

`Return a tuple in Python - (chickens, cows) and an array list - [chickens, cows]/{chickens, cows}
in all other languages`
<br>

If either the heads & legs is negative, the result of your calculation is negative or the
calculation is a float return "No solutions" (no valid cases), or [-1, -1] in COBOL.
<br>

In the form:
```
(Heads, Legs) = (72, 200)

VALID - (72, 200) =>             (44 , 28) 
                             (Chickens, Cows)

INVALID - (72, 201) => "No solutions"
```
<br>

However, `if 0 heads and 0 legs are given always return [0, 0]` since zero heads must give zero
animals.
<br>

There are many different ways to solve this, but they all give the same answer.
<br>

You will only be given integers types - however negative values (edge cases) will be given.
<br>

Happy coding!
