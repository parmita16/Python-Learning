# 2. 2D Array Slicing
import numpy as np

arr_2d = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
])

# 1. Second row
print(arr_2d[1])

# 2. Third column
print(arr_2d[:, 2])

# 3. Every alternate column
print(arr_2d[:, ::2])

# 4. Bottom-right 2×2 sub-array
print(arr_2d[-2:, -2:])