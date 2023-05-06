Problem description at Codewars can be found
[here](https://www.codewars.com/kata/55befc42bfe4d13ab1000007/train/python).

-------------

Implement a `GetNth()` function that takes a linked list and an integer index and returns the node
stored at the `Nth` index position. `GetNth()` uses the C numbering convention that the first node
is index 0, the second is index 1, ... and so on.
<br>

So for the list `42 -> 13 -> 666`, `GetNth(1)` should return `Node(13)`;
```
getNth(1 -> 2 -> 3 -> null, 0).data === 1
getNth(1 -> 2 -> 3 -> null, 1).data === 2
```
<br>

The index should be in the range `[0..length-1]`. If it is not, or if the list is empty, `GetNth()`
should throw/raise an exception (`ArgumentException` in C#, `InvalidArgumentException` in PHP,
`Exception` in Java).
<br>

Inspired by Stanford Professor Nick Parlante's excellent [Linked List
teachings](http://cslibrary.stanford.edu/103/LinkedListBasics.pdf).

[http://cslibrary.stanford.edu/103/LinkedListBasics.pdf](http://cslibrary.stanford.edu/103/LinkedListBasics.pdf)
<br>

[http://cslibrary.stanford.edu/105/LinkedListProblems.pdf](http://cslibrary.stanford.edu/105/LinkedListProblems.pdf)
