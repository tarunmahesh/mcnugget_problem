# McNugget Solver

## Overview

This repository contains a Jupyter notebook for solving the McNugget problem and its reverse. The McNugget problem involves finding the largest number of McNuggets that cannot be obtained using any combination of given pack sizes.

## Functions

### `mcnugget_solver(list1)`
Finds the largest number of McNuggets that cannot be obtained using any combination of the given pack sizes.

**Parameters:**
- `list1`: List of pack sizes (integers).

**Returns:**
- Largest non-obtainable number or a message if the result is infinite.

### `reverse_mcnugget_solver(x, list1)`
Finds the combination of packs that sum up to a given number of McNuggets.

**Parameters:**
- `x`: Target number of McNuggets (integer).
- `list1`: List of pack sizes (integers).

**Returns:**
- List of tuples indicating the pack sizes and their counts or a message if no solution exists.

## Example

```python
from mcnugget_solver import mcnugget_solver, reverse_mcnugget_solver

# Find largest non-obtainable number
print(mcnugget_solver([5, 9]))

# Find combination for target number
print(reverse_mcnugget_solver(23, [5, 9]))
