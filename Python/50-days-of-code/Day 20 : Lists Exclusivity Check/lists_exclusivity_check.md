## Day 20

**List XOR**

Define a function named `list_xor`. Your function should take **three** parameters: `n`, `list1` and `list2`.

Your function must return whether `n` is **exclusively in list1 or list2**.

In other words, if n is in both lists or in none of the lists, return `False`. If n is in only one of the lists, return `True`.

Examples : <br>
`list_xor(1, [1, 2, 3], [4, 5, 6])` should return `True`<br>
`list_xor(1, [0, 2, 3], [1, 5, 6])` should return `True`<br>
`list_xor(1, [1, 2, 3], [1, 5, 6])` should return `False`<br>
`list_xor(1, [0, 0, 0], [4, 5, 6])` should return `False`<br>