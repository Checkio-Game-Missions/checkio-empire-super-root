We have built the super computer and we need super problem for it.
Square roots, cube roots, 4th roots... each are too boring for the Laboratory mind.
He needs to find the super root! With your help he will almost certainly find it.

The super root of a number **N** is the number **x**,
such that **x<sup>x</sup>** = **N**.

The result should be accurate so that  **x<sup>x</sup> &asymp; N&plusmn;0.001**.
Or **N - 0.001 < x<sup>x</sup> < N + 0.001**.

**Input:** A number (N) as an integer.

**Output:** The super root (x) as a float or an integer.

**Example:**

```python
super_root(4) == 2
super_root(27) == 3
super_root(81) == 3.504339593597054
```

**How it is used:**

This concept can be useful for the cryptography.
And you will look how work your calculator then calculate roots.


**Precondition:**
```python
1 <= number <= 10 ** 10
```
