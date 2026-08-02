# 3. 3D Array Slicing
import numpy as np

arr_3d = np.arange(1, 25).reshape(2, 3, 4)

# 1. Second row from every 2D slice
print(arr_3d[:, 1, :])

# 2. Last column from every 2D slice
print(arr_3d[:, :, -1])

# 3. Top-left (2,2,2) sub-array
print(arr_3d[:, :2, :2])

# 4. Corners of first and last rows
print(arr_3d[:, [0, -1], :][:, :, [0, -1]])