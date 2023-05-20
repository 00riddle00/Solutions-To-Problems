Problem description at Codewars can be found
[here](https://www.codewars.com/kata/545b342082e55dc9da000051/train/python).

-------------

Create a method partition that accepts a list and a method/block. It should return two arrays: the
first, with all the elements for which the given block returned true, and the second for the
remaining elements.
<br>

Here's a simple Ruby example:
```
animals = ["cat", "dog", "duck", "cow", "donkey"]
partition(animals){|animal| animal.size == 3}
    #=> [["cat", "dog", "cow"], ["duck", "donkey"]]
```
<br>

The equivalent in Python would be:
```
animals = ['cat', 'dog', 'duck', 'cow', 'donkey']
partition(animals, lambda x: len(x) == 3)
    # (['cat', 'dog', 'cow'], ['duck', 'donkey'])
```
<br>

If you need help, here's a reference:
<br>

http://www.rubycuts.com/enum-partition
