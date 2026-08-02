# 1. 1D Array Slicing
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

# 1. Elements from index 2 to 6 (6 excluded)
print(arr[2:6])

# 2. Every second element
print(arr[::2])

# 3. Reverse the array
print(arr[::-1])

# 4. Last 4 elements
print(arr[-4:])

# 5. Index 1 to 7 with step 2
print(arr[1:8:2])