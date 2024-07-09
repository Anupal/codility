# Codility Training problems

### Tricks
- pivots
- hashsets
- lazy updates
- prefix sum
    - rolling sum
    - next occurence
- patterns within sublists
- stacks to store behavior in order
- the count of most frequent element will always be > n / 2

### Edge cases
1. Empty arrays
2. Modulo return values
3. Failure return values like -1
4. Return -1 for values larger than threshold
5. Check Loop bounds (0 -> n) or (1 -> n + 1)

## Nice Algos
### Kadanes algo
#### maximum sub-array (empty sub-array not permitted)
```python
def max_subarray(numbers):
    """Find the largest sum of any contiguous subarray."""
    best_sum = - infinity
    current_sum = 0
    for x in numbers:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum
```

#### maximum sub-array (empty sub-array permitted)
```python
best_sum = 0;
current_sum = max(0, current_sum + x)
```

### Binary Search
- Usual implementation gives the index of the target in the array.
- If not found, the index points to the smallest number larger than target in the array.
- If you need largest number smaller than target, just decrement i. If i is 0 then such a number doesn not exist.
