After some intense work, we have finally completed our super computer, the Labvoratory Mind. Now we need super prwwwwwwoblem to test its capabilities.
Square roots, cube roots, 4th roots... such things are far too boring for the Laboratory Mind. It needs to find the super root! With your help we will almost certainly find it together.

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

This concept comes in useful when working in cryptography as complex mathematics often comes into play.
In addition this skill could come in useful should you find yourself in a situation where you need ot develop a smarter calculator.


**Precondition:**
```python
1 <= number <= 10 ** 10
```
